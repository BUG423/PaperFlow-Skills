# Local Commands

## Locate Skill Tools

On this machine, the system `skill-creator` tools are normally under:

```text
C:/Users/李超越/.codex/skills/.system/skill-creator/scripts/
```

If the path changes, locate them with:

```powershell
Get-ChildItem -Force -Recurse -Filter init_skill.py "$HOME/.codex/skills"
Get-ChildItem -Force -Recurse -Filter quick_validate.py "$HOME/.codex/skills"
```

## Initialize A Skill

Use the initializer for new skills:

```powershell
python 'C:/Users/李超越/.codex/skills/.system/skill-creator/scripts/init_skill.py' my-skill --path 'C:/Users/李超越/.codex/skills' --resources references
```

Add only resource directories that are needed:

```powershell
python 'C:/Users/李超越/.codex/skills/.system/skill-creator/scripts/init_skill.py' my-skill --path 'C:/Users/李超越/.codex/skills' --resources scripts,references,assets
```

## PowerShell Quoting

In PowerShell, `$skill-name` inside double quotes can be treated as a variable expression. Use single quotes for interface values that contain `$`:

```powershell
python 'C:/Users/李超越/.codex/skills/.system/skill-creator/scripts/init_skill.py' my-skill --path 'C:/Users/李超越/.codex/skills' --interface display_name='My Skill' --interface short_description='Create a focused skill' --interface default_prompt='Use $my-skill to create a focused skill.'
```

If a generated `agents/openai.yaml` loses the skill name, edit it so the prompt explicitly includes `$my-skill`.

## Validate

Run the validator when available:

```powershell
python 'C:/Users/李超越/.codex/skills/.system/skill-creator/scripts/quick_validate.py' 'C:/Users/李超越/.codex/skills/my-skill'
```

If validation fails because Python package `yaml` is missing, report the dependency issue and perform the manual validation checklist in `references/design-checklist.md`. Install dependencies only when the user has asked for a fully automated local validator or the environment policy allows it.

## Inspect Created Files

Use these commands to review a skill without noisy output:

```powershell
Get-ChildItem -Force -Recurse -Name -LiteralPath 'C:/Users/李超越/.codex/skills/my-skill'
Get-Content -Raw -LiteralPath 'C:/Users/李超越/.codex/skills/my-skill/SKILL.md'
Get-Content -Raw -LiteralPath 'C:/Users/李超越/.codex/skills/my-skill/agents/openai.yaml'
```
