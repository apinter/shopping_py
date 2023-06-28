![build](https://github.com/apinter/shopping_py/actions/workflows/build.yml/badge.svg)

# Shopping List 🛒

A simple _Telegram_ bot to manage my shopping list.

Simple is likely to be an understatement since this thing is super primitive, but I don't need anything else `¯\_(ツ)_/¯`
The bot will write everything in a single file. It reads from this file, and changes this file when you add/remove items.

## Usage

```bash
 podman run \
        --name shopping-list \
        --label io.containers.autoupdate=registry \
        -e TG_BOT_TOKEN=12345:758932 \ ## generate the bot and token with Botfather
        -v shopping_list:/app/data:z docker.io/adathor/shopping-bot
```

Start chat with the bot, and run `/help` for all the options.
