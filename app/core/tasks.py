import logging

from celery import shared_task

from core.management.commands.conformance_alerts import \
    Command as conformance_alerts
from core.management.commands.consolidate_ledgers import \
    Command as consolidate_ledgers
from core.management.commands.load_index_agents import Command as load_index

logger = logging.getLogger('dict_config_logger')


@shared_task(name="workflow_for_xis")
def xis_workflow():
    """XIS automated workflow"""

    consolidate_ledgers_class = consolidate_ledgers()
    load_index_class = load_index()
    conformance_alerts_class = conformance_alerts()

    consolidate_ledgers_class.handle()
    load_index_class.handle()
    conformance_alerts_class.handle()

    logger.info('COMPLETED WORKFLOW')
