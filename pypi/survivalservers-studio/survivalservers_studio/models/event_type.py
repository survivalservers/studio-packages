from enum import StrEnum


class EventType(StrEnum):
    BACKUP_CHECK_FAILED = "backup.check_failed"
    BACKUP_EXPORT_READY = "backup.export_ready"
    BILLING_BUDGET_THRESHOLD = "billing.budget_threshold"
    BILLING_FREE_HOURS = "billing.free_hours"
    BILLING_INVOICE_CREATED = "billing.invoice_created"
    BILLING_PAYMENT_FAILED = "billing.payment_failed"
    BUILD_FAILED = "build.failed"
    BUILD_READY = "build.ready"
    BULK_ACTION_FINISHED = "bulk_action.finished"
    BULK_ACTION_PAUSED = "bulk_action.paused"
    BULK_ACTION_PROGRESS = "bulk_action.progress"
    BULK_ACTION_STARTED = "bulk_action.started"
    BULK_ACTION_STOPPED = "bulk_action.stopped"
    GAME_SERVER_DISK_HIGH = "game_server.disk_high"
    GAME_SERVER_FAILED = "game_server.failed"
    GAME_SERVER_MEMORY_HIGH = "game_server.memory_high"
    GAME_SERVER_PLAYERS_CHANGED = "game_server.players_changed"
    GAME_SERVER_RESTARTED = "game_server.restarted"
    GAME_SERVER_RUNNING = "game_server.running"
    GAME_SERVER_STARTING = "game_server.starting"
    GAME_SERVER_STOPPED = "game_server.stopped"
    GAME_SERVER_STOPPING = "game_server.stopping"
    PERSISTENT_SERVER_BACKUP_CREATED = "persistent_server.backup_created"
    PERSISTENT_SERVER_BACKUP_FAILED = "persistent_server.backup_failed"
    PERSISTENT_SERVER_FAILED = "persistent_server.failed"
    PERSISTENT_SERVER_KEEP_LIMIT_REACHED = "persistent_server.keep_limit_reached"
    PERSISTENT_SERVER_MOVED = "persistent_server.moved"
    PERSISTENT_SERVER_PAUSED = "persistent_server.paused"
    PERSISTENT_SERVER_RESTORED = "persistent_server.restored"
    PERSISTENT_SERVER_RESUMED = "persistent_server.resumed"
    PERSISTENT_SERVER_RESUMING = "persistent_server.resuming"
    PERSISTENT_SERVER_RUNNING = "persistent_server.running"
    PERSISTENT_SERVER_STARTING = "persistent_server.starting"
    PERSISTENT_SERVER_STOPPED = "persistent_server.stopped"
    PERSISTENT_SERVER_STOPPING = "persistent_server.stopping"
    POOL_EXHAUSTED = "pool.exhausted"
    POOL_STARTS_FAILING = "pool.starts_failing"
    REGION_STATUS_CHANGED = "region.status_changed"
    TEST_PING = "test.ping"
    VERSION_REGION_READY = "version.region_ready"

    def __str__(self) -> str:
        return str(self.value)

    @classmethod
    def _missing_(cls, value: object) -> "EventType | None":
        # The API adds values at any time: a value this version does not know is read as a value of its own.
        if not isinstance(value, str):
            return None
        unknown = str.__new__(cls, value)
        unknown._name_ = value
        unknown._value_ = value
        return unknown
