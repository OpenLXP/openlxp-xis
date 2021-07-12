import logging

from celery import shared_task

from core.management.commands.conformance_alerts import \
    Command as conformance_alerts
from core.management.commands.load_index_agents import Command as load_index
from core.management.commands.merge_metadata_in_composite_ledger import \
    Command as merge_metadata

logger = logging.getLogger('dict_config_logger')


@shared_task(name="workflow_for_xis")
def xis_workflow():
    """XIS automated workflow"""

    merge_metadata_class = merge_metadata()
    load_index_class = load_index()
    conformance_alerts_class = conformance_alerts()

    merge_metadata_class.handle()
    load_index_class.handle()
    conformance_alerts_class.handle()

    logger.info('COMPLETED WORKFLOW')
