from typing import List
from app.common.models import ClipboardEntry, Application
from loguru import logger


class ClipboardManager:
    def get_recent_entries(self, limit) -> List[ClipboardEntry]:
        logger.info("Getting recent entries...")
        return (
            ClipboardEntry.select()
            .order_by(ClipboardEntry.timestamp.desc())
            .limit(limit)
        )

    def add_new_entry(self, content: str, app_name: str = None) -> None:
        logger.info("Adding new entry {}...", content)
        application, created = Application.get_or_create(app_name=app_name)
        ClipboardEntry.create(content=content, source_app=application)

    def pin_entry(self, entry_id: int) -> None:
        logger.info("Pinning entry...")
        entry = ClipboardEntry.get_by_id(entry_id)
        entry.is_pinned = True
        entry.save()
