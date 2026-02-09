# Glossary (Repo Excerpt)

For the full glossary, see: https://github.com/instance001/Whatisthisgithub/blob/main/GLOSSARY.md

This file contains only the glossary entries for this repository. Mapping tag legends and global notes live in the full glossary.

## Chattymobile_v1
| Term | Alternate term(s) | Alt map | External map | Relation to existing terminology | What it is | What it is not | Source |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Chatty Mobile Seed Lock | Chatty mobile seed release | ~ | ~ | Prototype mobile assistant release | Android/Kivy seed release with persistent local memory (`memory.json`), auto-generated `config.json`, and Symbound alignment capsule `symbound.txt`; AGPL-3.0 | Not a production APK distribution with bundled weights; may not run reliably on all Android devices | Chattymobile_v1/README.md; Chattymobile_v1/main.py |
| Symbound capsule (mobile) | symbound.txt | = | ~ | Analogous to system prompt file | Text capsule holding alignment/override directives loaded into Chatty UI | Not code; not enforced policy beyond prompt usage | Chattymobile_v1/main.py |
| Local memory store (mobile) | memory.json | = | ~ | Comparable to session memory log | JSON history appended per exchange for persistence on device storage | Not encrypted or cloud-synced; not vector memory | Chattymobile_v1/main.py |
| Config seed (mobile) | config.json | = | ~ | Basic client config | Auto-created config with `api_key` and `model` defaulting to none/mistral-7b-instruct; enables optional Together API completions | Not a key manager; API calls skipped when key is none | Chattymobile_v1/main.py |
| Chatty mobile UI | Kivy UI | ~ | ~ | Standard chat UI implementation | Kivy-based interface with label output, text input, send button; supports Android app_storage_path | Not web-based; no background services | Chattymobile_v1/main.py |
