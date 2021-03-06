import * as _ from 'lodash';
import { connect } from 'react-redux';
import { withRouter } from 'react-router-dom';
import { Dispatch } from 'redux';

import * as actions from '../../actions/experiments';
import * as groupsActions from '../../actions/groups';
import * as searchActions from '../../actions/search';
import Experiments from '../../components/experiments/experiments';
import { ACTIONS } from '../../constants/actions';
import { AppState } from '../../constants/types';
import { isTrue } from '../../constants/utils';
import { ExperimentModel } from '../../models/experiment';
import { GroupModel } from '../../models/group';
import { SearchModel } from '../../models/search';
import { ARCHIVES, BOOKMARKS } from '../../utils/endpointList';
import { getErrorsGlobal } from '../../utils/errors';
import { getLastFetchedExperiments } from '../../utils/states';
import { getSuccessGlobal } from '../../utils/success';

interface OwnProps {
  user: string;
  projectName?: string;
  groupId?: number;
  useFilters?: boolean;
  showBookmarks?: boolean;
  showDeleted?: boolean;
  useCheckbox?: boolean;
  endpointList?: string;
  fetchData?: () => actions.ExperimentAction;
}

export function mapStateToProps(state: AppState, ownProps: OwnProps) {
  const results = getLastFetchedExperiments(state.experiments);

  const isLoading = isTrue(state.loadingIndicators.experiments.global.fetch);
  const isCreateLoading = isTrue(state.loadingIndicators.experiments.global.create);
  return {
    isCurrentUser: state.auth.user === ownProps.user,
    experiments: results.experiments,
    groupId: ownProps.groupId,
    count: results.count,
    useFilters: isTrue(ownProps.useFilters),
    showBookmarks: isTrue(ownProps.showBookmarks),
    showDeleted: isTrue(ownProps.showDeleted),
    useCheckbox: isTrue(ownProps.useCheckbox),
    endpointList: ownProps.endpointList,
    isLoading,
    isCreateLoading,
    errors: getErrorsGlobal(state.alerts.experiments.global, isLoading, ACTIONS.FETCH),
    createErrors: getErrorsGlobal(state.alerts.experiments.global, isLoading, ACTIONS.CREATE),
    createSuccess: getSuccessGlobal(state.alerts.experiments.global, isLoading, ACTIONS.CREATE),
  };
}

export interface DispatchProps {
  onCreate: (experiment: ExperimentModel) => actions.ExperimentAction;
  onDelete: (experimentName: string) => actions.ExperimentAction;
  onDeleteMany: (experimentIds: number[]) => actions.ExperimentAction;
  onStop: (experimentName: string) => actions.ExperimentAction;
  onArchive: (experimentName: string) => actions.ExperimentAction;
  onRestart: (experimentName: string) => actions.ExperimentAction;
  onRestore: (experimentName: string) => actions.ExperimentAction;
  onStopMany: (experimentIds: number[]) => actions.ExperimentAction;
  bookmark: (experimentName: string) => actions.ExperimentAction;
  unbookmark: (experimentName: string) => actions.ExperimentAction;
  onUpdate: (experiment: ExperimentModel) => actions.ExperimentAction;
  fetchData: (offset?: number, query?: string, sort?: string) => actions.ExperimentAction;
  fetchSearches: () => searchActions.SearchAction;
  createSearch: (data: SearchModel) => searchActions.SearchAction;
  deleteSearch: (searchId: number) => searchActions.SearchAction;
  createSelection: (data: GroupModel) => groupsActions.GroupAction;
  addToSelection: (selectionId: number, items: number[]) => groupsActions.GroupAction;
  removeFromSelection: (selectionId: number, items: number[]) => groupsActions.GroupAction;
}

export function mapDispatchToProps(dispatch: Dispatch<actions.ExperimentAction>, params: any): DispatchProps {
  return {
    onCreate: (experiment: ExperimentModel) => dispatch(actions.createExperiment(
      params.match.params.user,
      params.match.params.projectName,
      experiment,
      true)),
    onDelete: (experimentName: string) => dispatch(actions.deleteExperiment(experimentName)),
    onDeleteMany: (experimentIds: number[]) => {
      if (params.projectName) {
        return dispatch(actions.deleteExperiments(params.projectName, experimentIds));
      } else {
        throw new Error('Experiments container does not have project.');
      }
    },
    onStop: (experimentName: string) => dispatch(actions.stopExperiment(experimentName)),
    onArchive: (experimentName: string) => dispatch(actions.archiveExperiment(experimentName)),
    onRestart: (experimentName: string) => dispatch(actions.restartExperiment(experimentName, true)),
    onRestore: (experimentName: string) => dispatch(actions.restoreExperiment(experimentName)),
    onStopMany: (experimentIds: number[]) => {
      if (params.projectName) {
        return dispatch(actions.stopExperiments(params.projectName, experimentIds));
      } else {
        throw new Error('Experiments container does not have project.');
      }
    },
    bookmark: (experimentName: string) => dispatch(actions.bookmark(experimentName)),
    unbookmark: (experimentName: string) => dispatch(actions.unbookmark(experimentName)),
    onUpdate: (experiment: ExperimentModel) => dispatch(actions.updateExperimentSuccessActionCreator(experiment)),
    fetchSearches: () => {
      if (params.projectName) {
        return dispatch(searchActions.fetchExperimentSearches(params.projectName));
      } else {
        throw new Error('Experiments container does not have project.');
      }
    },
    createSearch: (data: SearchModel) => {
      if (params.projectName) {
        return dispatch(searchActions.createExperimentSearch(params.projectName, data));
      } else {
        throw new Error('Experiments container does not have project.');
      }
    },
    deleteSearch: (searchId: number) => {
      if (params.projectName) {
        return dispatch(searchActions.deleteExperimentSearch(params.projectName, searchId));
      } else {
        throw new Error('Experiments container does not have project.');
      }
    },
    createSelection: (data: GroupModel) => {
      if (params.projectName) {
        return dispatch(groupsActions.createGroup(
          params.match.params.user,
          params.match.params.projectName,
          data,
          true));
      } else {
        throw new Error('Experiments container does not have project.');
      }
    },
    addToSelection: (selectionId: number, items: number[]) => {
      if (params.projectName) {
        const data = {experiment_ids: items, operation: 'add'};
        const groupName = `${params.projectName}.${selectionId}`;
        return dispatch(groupsActions.updateSelection(groupName, data));
      } else {
        throw new Error('Experiments container does not have project.');
      }
    },
    removeFromSelection: (selectionId: number, items: number[]) => {
      if (params.projectName) {
        const data = {experiment_ids: items, operation: 'remove'};
        const groupName = `${params.projectName}.${selectionId}`;
        return dispatch(groupsActions.updateSelection(groupName, data));
      } else {
        throw new Error('Experiments container does not have project.');
      }
    },
    fetchData: (offset?: number,
                query?: string,
                sort?: string,
                extraFilters?: { [key: string]: number | boolean | string }) => {
      const filters: { [key: string]: number | boolean | string } = {};
      if (params.groupId) {
        filters.group = params.groupId;
      }
      if (extraFilters && (extraFilters.metrics === true || extraFilters.metrics === 'true')) {
        filters.metrics = extraFilters.metrics;
      }
      if (extraFilters && (extraFilters.declarations === true || extraFilters.declarations === 'true')) {
        filters.declarations = extraFilters.declarations;
      }
      if (extraFilters && (extraFilters.independent === true || extraFilters.independent === 'true')) {
        filters.independent = extraFilters.independent;
      }
      if (query) {
        filters.query = query;
      }
      if (sort) {
        filters.sort = sort;
      }
      if (offset) {
        filters.offset = offset;
      }
      if (_.isNil(params.projectName) && params.endpointList === BOOKMARKS) {
        return dispatch(actions.fetchBookmarkedExperiments(params.user, filters));
      } else if (_.isNil(params.projectName) && params.endpointList === ARCHIVES) {
        return dispatch(actions.fetchArchivedExperiments(params.user, filters));
      } else if (params.projectName) {
        return dispatch(actions.fetchExperiments(params.projectName, filters));
      } else {
        throw new Error('Experiments container expects either a project name or bookmarks or archives.');
      }
    }
  };
}

export default withRouter(connect(mapStateToProps, mapDispatchToProps)(Experiments));
