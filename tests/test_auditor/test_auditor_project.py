# pylint:disable=ungrouped-imports

from unittest.mock import patch

import pytest

import auditor

from event_manager.events import project as project_events
from factories.factory_projects import ProjectFactory
from tests.test_auditor.utils import AuditorBaseTest


@pytest.mark.auditor_mark
class AuditorProjectTest(AuditorBaseTest):
    """Testing subscribed events"""
    EVENTS = project_events.EVENTS

    def setUp(self):
        self.project = ProjectFactory()
        super().setUp()
        self.tested_events = {
            project_events.PROJECT_CREATED,
            project_events.PROJECT_UPDATED,
            project_events.PROJECT_DELETED,
            project_events.PROJECT_DELETED_TRIGGERED,
            project_events.PROJECT_VIEWED,
            project_events.PROJECT_ARCHIVED,
            project_events.PROJECT_RESTORED,
            project_events.PROJECT_UNBOOKMARKED,
            project_events.PROJECT_BOOKMARKED,
            project_events.PROJECT_SET_PUBLIC,
            project_events.PROJECT_SET_PRIVATE,
            project_events.PROJECT_EXPERIMENT_GROUPS_VIEWED,
            project_events.PROJECT_EXPERIMENTS_VIEWED,
            project_events.PROJECT_JOBS_VIEWED,
            project_events.PROJECT_BUILDS_VIEWED,
            project_events.PROJECT_TENSORBOARDS_VIEWED,
            project_events.PROJECT_NOTEBOOKS_VIEWED,
        }

    @patch('executor.executor_service.ExecutorService.record_event')
    @patch('notifier.service.NotifierService.record_event')
    @patch('tracker.service.TrackerService.record_event')
    @patch('activitylogs.service.ActivityLogService.record_event')
    def test_project_created(self,
                             activitylogs_record,
                             tracker_record,
                             notifier_record,
                             executor_record):
        auditor.record(event_type=project_events.PROJECT_CREATED,
                       instance=self.project)

        assert tracker_record.call_count == 1
        assert activitylogs_record.call_count == 1
        assert notifier_record.call_count == 0
        assert executor_record.call_count == 0

    @patch('executor.executor_service.ExecutorService.record_event')
    @patch('notifier.service.NotifierService.record_event')
    @patch('tracker.service.TrackerService.record_event')
    @patch('activitylogs.service.ActivityLogService.record_event')
    def test_project_updated(self,
                             activitylogs_record,
                             tracker_record,
                             notifier_record,
                             executor_record):
        auditor.record(event_type=project_events.PROJECT_UPDATED,
                       instance=self.project,
                       actor_name='foo',
                       actor_id=1)

        assert tracker_record.call_count == 1
        assert activitylogs_record.call_count == 1
        assert notifier_record.call_count == 0
        assert executor_record.call_count == 0

    @patch('executor.executor_service.ExecutorService.record_event')
    @patch('notifier.service.NotifierService.record_event')
    @patch('tracker.service.TrackerService.record_event')
    @patch('activitylogs.service.ActivityLogService.record_event')
    def test_project_deleted(self,
                             activitylogs_record,
                             tracker_record,
                             notifier_record,
                             executor_record):
        auditor.record(event_type=project_events.PROJECT_DELETED,
                       instance=self.project)

        assert tracker_record.call_count == 1
        assert activitylogs_record.call_count == 0
        assert notifier_record.call_count == 0
        assert executor_record.call_count == 0

    @patch('executor.executor_service.ExecutorService.record_event')
    @patch('notifier.service.NotifierService.record_event')
    @patch('tracker.service.TrackerService.record_event')
    @patch('activitylogs.service.ActivityLogService.record_event')
    def test_project_deleted_triggered(self,
                                       activitylogs_record,
                                       tracker_record,
                                       notifier_record,
                                       executor_record):
        auditor.record(event_type=project_events.PROJECT_DELETED_TRIGGERED,
                       instance=self.project,
                       actor_name='foo',
                       actor_id=1)

        assert tracker_record.call_count == 1
        assert activitylogs_record.call_count == 1
        assert notifier_record.call_count == 0
        assert executor_record.call_count == 0

    @patch('executor.executor_service.ExecutorService.record_event')
    @patch('notifier.service.NotifierService.record_event')
    @patch('tracker.service.TrackerService.record_event')
    @patch('activitylogs.service.ActivityLogService.record_event')
    def test_project_viewed(self,
                            activitylogs_record,
                            tracker_record,
                            notifier_record,
                            executor_record):
        auditor.record(event_type=project_events.PROJECT_VIEWED,
                       instance=self.project,
                       actor_name='foo',
                       actor_id=1)

        assert tracker_record.call_count == 1
        assert activitylogs_record.call_count == 1
        assert notifier_record.call_count == 0
        assert executor_record.call_count == 0

    @patch('executor.executor_service.ExecutorService.record_event')
    @patch('notifier.service.NotifierService.record_event')
    @patch('tracker.service.TrackerService.record_event')
    @patch('activitylogs.service.ActivityLogService.record_event')
    def test_project_archived(self,
                              activitylogs_record,
                              tracker_record,
                              notifier_record,
                              executor_record):
        auditor.record(event_type=project_events.PROJECT_ARCHIVED,
                       instance=self.project,
                       actor_name='foo',
                       actor_id=1)

        assert tracker_record.call_count == 1
        assert activitylogs_record.call_count == 1
        assert notifier_record.call_count == 0
        assert executor_record.call_count == 0

    @patch('executor.executor_service.ExecutorService.record_event')
    @patch('notifier.service.NotifierService.record_event')
    @patch('tracker.service.TrackerService.record_event')
    @patch('activitylogs.service.ActivityLogService.record_event')
    def test_project_restored(self,
                              activitylogs_record,
                              tracker_record,
                              notifier_record,
                              executor_record):
        auditor.record(event_type=project_events.PROJECT_RESTORED,
                       instance=self.project,
                       actor_name='foo',
                       actor_id=1)

        assert tracker_record.call_count == 1
        assert activitylogs_record.call_count == 1
        assert notifier_record.call_count == 0
        assert executor_record.call_count == 0

    @patch('executor.executor_service.ExecutorService.record_event')
    @patch('notifier.service.NotifierService.record_event')
    @patch('tracker.service.TrackerService.record_event')
    @patch('activitylogs.service.ActivityLogService.record_event')
    def test_project_unbookmarked(self,
                                  activitylogs_record,
                                  tracker_record,
                                  notifier_record,
                                  executor_record):
        auditor.record(event_type=project_events.PROJECT_UNBOOKMARKED,
                       instance=self.project,
                       actor_name='foo',
                       actor_id=1)

        assert tracker_record.call_count == 1
        assert activitylogs_record.call_count == 1
        assert notifier_record.call_count == 0
        assert executor_record.call_count == 0

    @patch('executor.executor_service.ExecutorService.record_event')
    @patch('notifier.service.NotifierService.record_event')
    @patch('tracker.service.TrackerService.record_event')
    @patch('activitylogs.service.ActivityLogService.record_event')
    def test_project_bookmarked(self,
                                activitylogs_record,
                                tracker_record,
                                notifier_record,
                                executor_record):
        auditor.record(event_type=project_events.PROJECT_BOOKMARKED,
                       instance=self.project,
                       actor_name='foo',
                       actor_id=1)

        assert tracker_record.call_count == 1
        assert activitylogs_record.call_count == 1
        assert notifier_record.call_count == 0
        assert executor_record.call_count == 0

    @patch('executor.executor_service.ExecutorService.record_event')
    @patch('notifier.service.NotifierService.record_event')
    @patch('tracker.service.TrackerService.record_event')
    @patch('activitylogs.service.ActivityLogService.record_event')
    def test_project_set_public(self,
                                activitylogs_record,
                                tracker_record,
                                notifier_record,
                                executor_record):
        auditor.record(event_type=project_events.PROJECT_SET_PUBLIC,
                       instance=self.project,
                       actor_id=1)

        assert tracker_record.call_count == 1
        assert activitylogs_record.call_count == 0
        assert notifier_record.call_count == 0
        assert executor_record.call_count == 0

    @patch('executor.executor_service.ExecutorService.record_event')
    @patch('notifier.service.NotifierService.record_event')
    @patch('tracker.service.TrackerService.record_event')
    @patch('activitylogs.service.ActivityLogService.record_event')
    def test_project_set_private(self,
                                 activitylogs_record,
                                 tracker_record,
                                 notifier_record,
                                 executor_record):
        auditor.record(event_type=project_events.PROJECT_SET_PRIVATE,
                       instance=self.project,
                       actor_id=1)

        assert tracker_record.call_count == 1
        assert activitylogs_record.call_count == 0
        assert notifier_record.call_count == 0
        assert executor_record.call_count == 0

    @patch('executor.executor_service.ExecutorService.record_event')
    @patch('notifier.service.NotifierService.record_event')
    @patch('tracker.service.TrackerService.record_event')
    @patch('activitylogs.service.ActivityLogService.record_event')
    def test_project_experiment_groups_viewed(self,
                                              activitylogs_record,
                                              tracker_record,
                                              notifier_record,
                                              executor_record):
        auditor.record(event_type=project_events.PROJECT_EXPERIMENT_GROUPS_VIEWED,
                       instance=self.project,
                       actor_id=1,
                       actor_name='foo')

        assert tracker_record.call_count == 1
        assert activitylogs_record.call_count == 1
        assert notifier_record.call_count == 0
        assert executor_record.call_count == 0

    @patch('executor.executor_service.ExecutorService.record_event')
    @patch('notifier.service.NotifierService.record_event')
    @patch('tracker.service.TrackerService.record_event')
    @patch('activitylogs.service.ActivityLogService.record_event')
    def test_project_experiments_viewed(self,
                                        activitylogs_record,
                                        tracker_record,
                                        notifier_record,
                                        executor_record):
        auditor.record(event_type=project_events.PROJECT_EXPERIMENTS_VIEWED,
                       instance=self.project,
                       actor_name='foo',
                       actor_id=1)

        assert tracker_record.call_count == 1
        assert activitylogs_record.call_count == 1
        assert notifier_record.call_count == 0
        assert executor_record.call_count == 0

    @patch('executor.executor_service.ExecutorService.record_event')
    @patch('notifier.service.NotifierService.record_event')
    @patch('tracker.service.TrackerService.record_event')
    @patch('activitylogs.service.ActivityLogService.record_event')
    def test_project_jobs_viewed(self,
                                 activitylogs_record,
                                 tracker_record,
                                 notifier_record,
                                 executor_record):
        auditor.record(event_type=project_events.PROJECT_JOBS_VIEWED,
                       instance=self.project,
                       actor_id=1,
                       actor_name='foo')

        assert tracker_record.call_count == 1
        assert activitylogs_record.call_count == 1
        assert notifier_record.call_count == 0
        assert executor_record.call_count == 0

    @patch('executor.executor_service.ExecutorService.record_event')
    @patch('notifier.service.NotifierService.record_event')
    @patch('tracker.service.TrackerService.record_event')
    @patch('activitylogs.service.ActivityLogService.record_event')
    def test_project_builds_viewed(self,
                                   activitylogs_record,
                                   tracker_record,
                                   notifier_record,
                                   executor_record):
        auditor.record(event_type=project_events.PROJECT_BUILDS_VIEWED,
                       instance=self.project,
                       actor_id=1,
                       actor_name='foo')

        assert tracker_record.call_count == 1
        assert activitylogs_record.call_count == 1
        assert notifier_record.call_count == 0
        assert executor_record.call_count == 0

    @patch('executor.executor_service.ExecutorService.record_event')
    @patch('notifier.service.NotifierService.record_event')
    @patch('tracker.service.TrackerService.record_event')
    @patch('activitylogs.service.ActivityLogService.record_event')
    def test_project_tensorboards_viewed(self,
                                         activitylogs_record,
                                         tracker_record,
                                         notifier_record,
                                         executor_record):
        auditor.record(event_type=project_events.PROJECT_TENSORBOARDS_VIEWED,
                       instance=self.project,
                       actor_id=1,
                       actor_name='foo')

        assert tracker_record.call_count == 1
        assert activitylogs_record.call_count == 1
        assert notifier_record.call_count == 0
        assert executor_record.call_count == 0

    @patch('executor.executor_service.ExecutorService.record_event')
    @patch('notifier.service.NotifierService.record_event')
    @patch('tracker.service.TrackerService.record_event')
    @patch('activitylogs.service.ActivityLogService.record_event')
    def test_project_notebooks_viewed(self,
                                      activitylogs_record,
                                      tracker_record,
                                      notifier_record,
                                      executor_record):
        auditor.record(event_type=project_events.PROJECT_NOTEBOOKS_VIEWED,
                       instance=self.project,
                       actor_id=1,
                       actor_name='foo')

        assert tracker_record.call_count == 1
        assert activitylogs_record.call_count == 1
        assert notifier_record.call_count == 0
        assert executor_record.call_count == 0


del AuditorBaseTest
