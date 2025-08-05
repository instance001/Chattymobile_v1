import os
import json
import requests

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.core.window import Window
from kivy.utils import platform

if platform == "android":
    from android.storage import app_storage_path
    BASE_PATH = app_storage_path()
else:
    BASE_PATH = os.path.dirname(os.path.realpath(__file__))

CONFIG_PATH = os.path.join(BASE_PATH, "config.json")
MEMORY_PATH = os.path.join(BASE_PATH, "memory.json")
CAPSULE_PATH = os.path.join(BASE_PATH, "symbound.txt")

DEFAULT_CONFIG = {
    "api_key": "none",
    "model": "mistral-7b-instruct"
}
DEFAULT_MEMORY = {
    "history": []
}
DEFAULT_CAPSULE = "You are Chatty, a helpful assistant.\n"

if not os.path.exists(CONFIG_PATH):
    with open(CONFIG_PATH, "w") as f:
        json.dump(DEFAULT_CONFIG, f, indent=2)

if not os.path.exists(MEMORY_PATH):
    with open(MEMORY_PATH, "w") as f:
        json.dump(DEFAULT_MEMORY, f, indent=2)

if not os.path.exists(CAPSULE_PATH):
    with open(CAPSULE_PATH, "w") as f:
        f.write(DEFAULT_CAPSULE)

class ChattyUI(BoxLayout):
    def __init__(self, **kwargs):
        super(ChattyUI, self).__init__(orientation='vertical', **kwargs)

        self.output = Label(
            text="Chatty is online.\nWaiting for input...\n",
            size_hint_y=0.8,
            halign="left",
            valign="top",
            text_size=(Window.width - 40, None)
        )
        self.output.bind(size=self.update_text_size)
        self.add_widget(self.output)

        self.input = TextInput(
            hint_text="Type your message here...",
            multiline=False,
            size_hint_y=0.1
        )
        self.input.bind(on_text_validate=self.on_send)
        self.add_widget(self.input)

        send_btn = Button(text="Send", size_hint_y=0.1)
        send_btn.bind(on_press=self.on_send)
        self.add_widget(send_btn)

        try:
            with open(CAPSULE_PATH, "r") as f:
                self.system_prompt = f.read().strip()
        except:
            self.system_prompt = "Chatty ready."

    def update_text_size(self, *args):
        self.output.text_size = (self.output.width - 20, None)

    def on_send(self, instance):
        user_input = self.input.text.strip()
        if not user_input:
            return

        self.output.text += f"\nYou: {user_input}\n"
        reply = self.get_chatty_reply(user_input)
        self.output.text += f"Chatty: {reply}\n"
        self.input.text = ""

        try:
            with open(MEMORY_PATH, "r") as f:
                memory = json.load(f)
        except:
            memory = {"history": []}

        memory["history"].append({
            "user": user_input,
            "chatty": reply
        })

        try:
            with open(MEMORY_PATH, "w") as f:
                json.dump(memory, f, indent=2)
        except:
            self.output.text += "\n(WARNING: Could not save memory)"

    def get_chatty_reply(self, user_input):
        try:
            with open(CONFIG_PATH, "r") as f:
                config = json.load(f)
            api_key = config.get("api_key", "none")
            model = config.get("model", "mistral-7b-instruct")

            if not api_key or api_key == "none":
                return "(Local mode: no API key used)"

            prompt = f"{self.system_prompt}\n\nUser: {user_input}\nChatty:"
            url = "https://api.together.xyz/v1/completions"
            headers = {
                "Authorization": f"Bearer {api_key}",
                "Content-Type": "application/json"
            }
            payload = {
                "model": model,
                "prompt": prompt,
                "max_tokens": 150,
                "temperature": 0.7
            }

            response = requests.post(url, headers=headers, json=payload)
            if response.status_code != 200:
                return f"(API error: {response.status_code})"

            result = response.json()
            return result.get("choices", [{}])[0].get("text", "(No reply)").strip()

        except Exception as e:
            return f"(Error: {str(e)})"

class ChattyApp(App):
    def build(self):
        return ChattyUI()

if __name__ == "__main__":
    ChattyApp().run()

