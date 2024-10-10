import asyncio
import docker
from argparse import ArgumentParser

from aiogram import Bot
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

from sqlalchemy import Table, Column, Integer, String

#Aiogram
def create_parser() -> ArgumentParser:
    parser = ArgumentParser()
    parser.add_argument("--token", help="Telegram Bot API Token")
    parser.add_argument("--chat-id", type=int, help="Target chat id")
    parser.add_argument("--message", "-m", help="Message text to sent", default="Hello, World!")

    return parser


async def main():
    parser = create_parser()
    ns = parser.parse_args()

    token = ns.token
    chat_id = ns.chat_id
    message = ns.message

    async with Bot(
            token=token,
            default=DefaultBotProperties(
                parse_mode=ParseMode.HTML,
            ),
    ) as bot:
        await bot.send_message(chat_id=chat_id, text=message)


if __name__ == "__main__":
    asyncio.run(main())

#SQLAlchemy

user = Table(
    "user",
    metadata_obj,
    Column("user_id", Integer, primary_key=True),
    Column("user_name", String(16), nullable=False),
    Column("email_address", String(60)),
    Column("nickname", String(50), nullable=False),
)


#Docker

client = docker.from_env()
client.containers.run('alpine', 'echo hello world')
b'hello world\n'