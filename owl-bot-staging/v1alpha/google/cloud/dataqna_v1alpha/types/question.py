# -*- coding: utf-8 -*-
# Copyright 2022 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
from __future__ import annotations

from typing import MutableMapping, MutableSequence

import proto  # type: ignore

from google.cloud.dataqna_v1alpha.types import annotated_string
from google.protobuf import any_pb2  # type: ignore
from google.protobuf import timestamp_pb2  # type: ignore
from google.rpc import status_pb2  # type: ignore


__protobuf__ = proto.module(
    package='google.cloud.dataqna.v1alpha',
    manifest={
        'InterpretEntity',
        'Question',
        'InterpretError',
        'ExecutionInfo',
        'BigQueryJob',
        'Interpretation',
        'DataQuery',
        'HumanReadable',
        'InterpretationStructure',
        'DebugFlags',
    },
)


class InterpretEntity(proto.Enum):
    r"""Query entities of an interpretation.

    Values:
        INTERPRET_ENTITY_UNSPECIFIED (0):
            No interpret entity was specified.
        DIMENSION (1):
            A dimenstion entity.
        METRIC (2):
            A metric entity.
    """
    INTERPRET_ENTITY_UNSPECIFIED = 0
    DIMENSION = 1
    METRIC = 2


class Question(proto.Message):
    r"""The question resource represents a natural language query,
    its settings, understanding generated by the system, and answer
    retrieval status. A question cannot be modified.

    Attributes:
        name (str):
            Output only. Immutable. The unique identifier for the
            Question. The ID is server-generated. Example:
            ``projects/foo/locations/bar/questions/123``
        scopes (MutableSequence[str]):
            Required. Immutable. Scopes to be used for the question. A
            scope defines the relevant data set scope. It can be a
            reference to a specific data source or a collection of data
            sources. Currently, support is limited to a single BigQuery
            table. There must be exactly one ``scopes`` element.

            Example:
            ``//bigquery.googleapis.com/projects/test-project/datasets/foo/tables/bar``
        query (str):
            Required. Immutable. The query in natural
            language.
        data_source_annotations (MutableSequence[str]):
            A list of annotations to use instead of the
            default annotation of a data source (set in the
            data source reference resource). There must not
            be more than one annotation with the same data
            source reference.
        interpret_error (google.cloud.dataqna_v1alpha.types.InterpretError):
            An error field explaining why interpretation
            failed. This is only populated if the
            interpretation failed.
            Note: This is different from getting a status
            error on the request itself. This is not a
            client or server error and the Question resource
            is still persisted, but the service could not
            interpret the question. Clients should present
            the error to the user so the user can rephrase
            the question.
        interpretations (MutableSequence[google.cloud.dataqna_v1alpha.types.Interpretation]):
            A list of interpretations for this question.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Time when the question was created.
        user_email (str):
            Output only. The e-mail address of the user
            that created this question.
        debug_flags (google.cloud.dataqna_v1alpha.types.DebugFlags):
            Input only. Immutable. Flags to request
            additional information for debugging purposes.
        debug_info (google.protobuf.any_pb2.Any):
            Top level debug information.
            This will be stored as the type
            DebugInformation. Using Any so clients don't
            need to pull in anything inside the debug
            message.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    scopes: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=2,
    )
    query: str = proto.Field(
        proto.STRING,
        number=3,
    )
    data_source_annotations: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=4,
    )
    interpret_error: 'InterpretError' = proto.Field(
        proto.MESSAGE,
        number=5,
        message='InterpretError',
    )
    interpretations: MutableSequence['Interpretation'] = proto.RepeatedField(
        proto.MESSAGE,
        number=6,
        message='Interpretation',
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=7,
        message=timestamp_pb2.Timestamp,
    )
    user_email: str = proto.Field(
        proto.STRING,
        number=8,
    )
    debug_flags: 'DebugFlags' = proto.Field(
        proto.MESSAGE,
        number=9,
        message='DebugFlags',
    )
    debug_info: any_pb2.Any = proto.Field(
        proto.MESSAGE,
        number=10,
        message=any_pb2.Any,
    )


class InterpretError(proto.Message):
    r"""Details on the failure to interpret the question.

    Attributes:
        message (str):
            Error message explaining why this question
            could not be interpreted.
        code (google.cloud.dataqna_v1alpha.types.InterpretError.InterpretErrorCode):
            The code for the error category why the
            interpretation failed.
        details (google.cloud.dataqna_v1alpha.types.InterpretError.InterpretErrorDetails):
            Details on interpretation failure.
    """
    class InterpretErrorCode(proto.Enum):
        r"""The interpret error code provides an error category why the
        interpretation failed.

        Values:
            INTERPRET_ERROR_CODE_UNSPECIFIED (0):
                No interpret error code was specified.
            INVALID_QUERY (1):
                The query is not valid.
            FAILED_TO_UNDERSTAND (2):
                The interpreter failed to understand the
                question. For example, because it was too
                ambiguous.
            FAILED_TO_ANSWER (3):
                The interpreter could understand the
                question, but was not able to arrive at an
                answer. For example, because a requested
                operation is not supported.
        """
        INTERPRET_ERROR_CODE_UNSPECIFIED = 0
        INVALID_QUERY = 1
        FAILED_TO_UNDERSTAND = 2
        FAILED_TO_ANSWER = 3

    class InterpretErrorDetails(proto.Message):
        r"""Details on interpretation failure.

        Attributes:
            unsupported_details (google.cloud.dataqna_v1alpha.types.InterpretError.InterpretUnsupportedDetails):
                Populated if parts of the query are
                unsupported.
            incomplete_query_details (google.cloud.dataqna_v1alpha.types.InterpretError.InterpretIncompleteQueryDetails):
                Populated if the query is incomplete.
            ambiguity_details (google.cloud.dataqna_v1alpha.types.InterpretError.InterpretAmbiguityDetails):
                Populated if the query was too ambiguous.
        """

        unsupported_details: 'InterpretError.InterpretUnsupportedDetails' = proto.Field(
            proto.MESSAGE,
            number=1,
            message='InterpretError.InterpretUnsupportedDetails',
        )
        incomplete_query_details: 'InterpretError.InterpretIncompleteQueryDetails' = proto.Field(
            proto.MESSAGE,
            number=2,
            message='InterpretError.InterpretIncompleteQueryDetails',
        )
        ambiguity_details: 'InterpretError.InterpretAmbiguityDetails' = proto.Field(
            proto.MESSAGE,
            number=3,
            message='InterpretError.InterpretAmbiguityDetails',
        )

    class InterpretUnsupportedDetails(proto.Message):
        r"""Details about unsupported parts in a query.

        Attributes:
            operators (MutableSequence[str]):
                Unsupported operators. For example: median.
            intent (MutableSequence[str]):
                Unsupported intents.
        """

        operators: MutableSequence[str] = proto.RepeatedField(
            proto.STRING,
            number=1,
        )
        intent: MutableSequence[str] = proto.RepeatedField(
            proto.STRING,
            number=2,
        )

    class InterpretIncompleteQueryDetails(proto.Message):
        r"""Details about an incomplete query.

        Attributes:
            entities (MutableSequence[google.cloud.dataqna_v1alpha.types.InterpretEntity]):
                List of missing interpret entities.
        """

        entities: MutableSequence['InterpretEntity'] = proto.RepeatedField(
            proto.ENUM,
            number=1,
            enum='InterpretEntity',
        )

    class InterpretAmbiguityDetails(proto.Message):
        r"""Details about a query that was too ambiguous. Currently, the
        message has no fields and its presence signals that there was
        ambiguity.

        """

    message: str = proto.Field(
        proto.STRING,
        number=1,
    )
    code: InterpretErrorCode = proto.Field(
        proto.ENUM,
        number=2,
        enum=InterpretErrorCode,
    )
    details: InterpretErrorDetails = proto.Field(
        proto.MESSAGE,
        number=3,
        message=InterpretErrorDetails,
    )


class ExecutionInfo(proto.Message):
    r"""Information about the backend status (such as BigQuery) of
    the execution.

    Attributes:
        job_creation_status (google.rpc.status_pb2.Status):
            Status returned by the backend when the job
            was created.
        job_execution_state (google.cloud.dataqna_v1alpha.types.ExecutionInfo.JobExecutionState):
            Status of the job execution.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Time when the execution was triggered.
        bigquery_job (google.cloud.dataqna_v1alpha.types.BigQueryJob):
            BigQuery job information.
            Future versions will have different backends.
            Hence, clients must make sure they can handle it
            when this field is not populated.
    """
    class JobExecutionState(proto.Enum):
        r"""Enum of possible job execution statuses.

        Values:
            JOB_EXECUTION_STATE_UNSPECIFIED (0):
                No job execution was specified.
            NOT_EXECUTED (1):
                No job execution was requested, yet.
            RUNNING (2):
                The job is running.
            SUCCEEDED (3):
                The job completed successfully.
            FAILED (4):
                The job completed unsuccessfully.
        """
        JOB_EXECUTION_STATE_UNSPECIFIED = 0
        NOT_EXECUTED = 1
        RUNNING = 2
        SUCCEEDED = 3
        FAILED = 4

    job_creation_status: status_pb2.Status = proto.Field(
        proto.MESSAGE,
        number=1,
        message=status_pb2.Status,
    )
    job_execution_state: JobExecutionState = proto.Field(
        proto.ENUM,
        number=2,
        enum=JobExecutionState,
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=3,
        message=timestamp_pb2.Timestamp,
    )
    bigquery_job: 'BigQueryJob' = proto.Field(
        proto.MESSAGE,
        number=4,
        message='BigQueryJob',
    )


class BigQueryJob(proto.Message):
    r"""BigQuery job information. This can be used to query the BigQuery API
    and retrieve the current job's status (using
    `jobs.get <https://cloud.google.com/bigquery/docs/reference/rest/v2/jobs/get>`__).

    Attributes:
        job_id (str):
            The job ID.
        project_id (str):
            The project ID of the job.
        location (str):
            The location where the job is running.
    """

    job_id: str = proto.Field(
        proto.STRING,
        number=1,
    )
    project_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    location: str = proto.Field(
        proto.STRING,
        number=3,
    )


class Interpretation(proto.Message):
    r"""An interpretation of a natural language query.

    Attributes:
        data_sources (MutableSequence[str]):
            List of data sources used in the current
            understanding.
        confidence (float):
            The level of confidence that one of the interpretations is
            correct. This is a value in the range [0, 1] where a value
            of 0.5 or below is to be considered a low confidence.
        unused_phrases (MutableSequence[str]):
            A list of unused phrases. Clients should
            display a Did You Mean (DYM)  dialog if this is
            non-empty, even if this is the only
            interpretation.
        human_readable (google.cloud.dataqna_v1alpha.types.HumanReadable):
            Human readable representation of the query.
        interpretation_structure (google.cloud.dataqna_v1alpha.types.InterpretationStructure):
            Information about the interpretation
            structure that helps to understand and visualize
            the response.
        data_query (google.cloud.dataqna_v1alpha.types.DataQuery):
            Representation of the data query to be sent
            to the backend.
        execution_info (google.cloud.dataqna_v1alpha.types.ExecutionInfo):
            Information about the backend response. This
            is populated only if execution of an
            interpretation was requested.
    """

    data_sources: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=1,
    )
    confidence: float = proto.Field(
        proto.DOUBLE,
        number=2,
    )
    unused_phrases: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )
    human_readable: 'HumanReadable' = proto.Field(
        proto.MESSAGE,
        number=4,
        message='HumanReadable',
    )
    interpretation_structure: 'InterpretationStructure' = proto.Field(
        proto.MESSAGE,
        number=5,
        message='InterpretationStructure',
    )
    data_query: 'DataQuery' = proto.Field(
        proto.MESSAGE,
        number=6,
        message='DataQuery',
    )
    execution_info: 'ExecutionInfo' = proto.Field(
        proto.MESSAGE,
        number=7,
        message='ExecutionInfo',
    )


class DataQuery(proto.Message):
    r"""Representation of the data query for the backend. This is provided
    for informational purposes only. Clients should not use it to send
    it to the backend directly, but rather use the ``execute`` RPC to
    trigger the execution. Using the ``execute`` RPC is needed in order
    to track the state of a question and report on it correctly to the
    data administrators.

    Attributes:
        sql (str):
            The generated SQL query to be sent to the
            backend.
    """

    sql: str = proto.Field(
        proto.STRING,
        number=1,
    )


class HumanReadable(proto.Message):
    r"""Human readable interpretation.

    Attributes:
        generated_interpretation (google.cloud.dataqna_v1alpha.types.AnnotatedString):
            Generated query explaining the
            interpretation.
        original_question (google.cloud.dataqna_v1alpha.types.AnnotatedString):
            Annotations on the original query.
    """

    generated_interpretation: annotated_string.AnnotatedString = proto.Field(
        proto.MESSAGE,
        number=1,
        message=annotated_string.AnnotatedString,
    )
    original_question: annotated_string.AnnotatedString = proto.Field(
        proto.MESSAGE,
        number=2,
        message=annotated_string.AnnotatedString,
    )


class InterpretationStructure(proto.Message):
    r"""Information about the interpretation structure that helps to
    understand and visualize the response.

    Attributes:
        visualization_types (MutableSequence[google.cloud.dataqna_v1alpha.types.InterpretationStructure.VisualizationType]):
            List of possible visualization types to apply
            for this interpretation. The order has no
            relevance.
        column_info (MutableSequence[google.cloud.dataqna_v1alpha.types.InterpretationStructure.ColumnInfo]):
            Information about the output columns, that
            is, the columns that will be returned by the
            backend.
    """
    class VisualizationType(proto.Enum):
        r"""Enumeration of visualzation types to use for query response
        data.

        Values:
            VISUALIZATION_TYPE_UNSPECIFIED (0):
                No visualization type was specified.
            TABLE (1):
                Show a table.
            BAR_CHART (2):
                Show a `bar
                chart <https://developers.google.com/chart/interactive/docs/gallery/barchart>`__.
            COLUMN_CHART (3):
                Show a `column
                chart <https://developers.google.com/chart/interactive/docs/gallery/columnchart>`__.
            TIMELINE (4):
                Show a
                `timeline <https://developers.google.com/chart/interactive/docs/gallery/timeline>`__.
            SCATTER_PLOT (5):
                Show a `scatter
                plot <https://developers.google.com/chart/interactive/docs/gallery/scatterchart>`__.
            PIE_CHART (6):
                Show a `pie
                chart <https://developers.google.com/chart/interactive/docs/gallery/piechart>`__.
            LINE_CHART (7):
                Show a `line
                chart <https://developers.google.com/chart/interactive/docs/gallery/linechart>`__.
            AREA_CHART (8):
                Show an `area
                chart <https://developers.google.com/chart/interactive/docs/gallery/areachart>`__.
            COMBO_CHART (9):
                Show a `combo
                chart <https://developers.google.com/chart/interactive/docs/gallery/combochart>`__.
            HISTOGRAM (10):
                Show a
                `histogram <https://developers.google.com/chart/interactive/docs/gallery/histogram>`__.
            GENERIC_CHART (11):
                This denotes queries when the user has not
                specified the particular type of chart and has
                mentioned only a generic chart name such as
                "Chart", "Plot", "Graph", etc. This will
                differentiate it from specific charting terms
                such as "Bar chart", "Pie chart", etc.
            CHART_NOT_UNDERSTOOD (12):
                The user tried to specify a chart type, but
                the interpreter could not understand the type.
                The client should display a generic chart and
                may give a hint to the user that the requested
                type was not understood.
        """
        VISUALIZATION_TYPE_UNSPECIFIED = 0
        TABLE = 1
        BAR_CHART = 2
        COLUMN_CHART = 3
        TIMELINE = 4
        SCATTER_PLOT = 5
        PIE_CHART = 6
        LINE_CHART = 7
        AREA_CHART = 8
        COMBO_CHART = 9
        HISTOGRAM = 10
        GENERIC_CHART = 11
        CHART_NOT_UNDERSTOOD = 12

    class ColumnInfo(proto.Message):
        r"""Information about a column.

        Attributes:
            output_alias (str):
                The alias of the output column as used by the
                backend. For example, the field name in the
                schema provided in the query response in
                BigQuery.
            display_name (str):
                Human readable name of the output column.
        """

        output_alias: str = proto.Field(
            proto.STRING,
            number=1,
        )
        display_name: str = proto.Field(
            proto.STRING,
            number=2,
        )

    visualization_types: MutableSequence[VisualizationType] = proto.RepeatedField(
        proto.ENUM,
        number=1,
        enum=VisualizationType,
    )
    column_info: MutableSequence[ColumnInfo] = proto.RepeatedField(
        proto.MESSAGE,
        number=2,
        message=ColumnInfo,
    )


class DebugFlags(proto.Message):
    r"""Configuriation of debug flags.

    Attributes:
        include_va_query (bool):
            Whether to include the original VAQuery.
        include_nested_va_query (bool):
            Whether to include the original nested
            VAQuery.
        include_human_interpretation (bool):
            Whether to include the original human
            interpretation strings generated by Analyza.
        include_aqua_debug_response (bool):
            Whether to include the Aqua debug response.
        time_override (int):
            The time in milliseconds from Unix epoch to be used to
            process the query. This is useful for testing the queries at
            different time period. If not set or time_override <= 0,
            then the current time is used.
        is_internal_google_user (bool):
            Set to true if request is initiated by an
            internal Google user.
        ignore_cache (bool):
            Determines whether cache needs to be ignored.
            If set to true, cache won't be queried and
            updated.
        include_search_entities_rpc (bool):
            Whether to include the request/response pair
            from the call to the EntityIndex for
            SearchEntities.
        include_list_column_annotations_rpc (bool):
            Whether to include the request/response pair
            from the call to the Annotations service for
            ListColumnAnnotations.
        include_virtual_analyst_entities (bool):
            Whether to include the entity list passed to
            Analyza.
        include_table_list (bool):
            Whether to include the table list.
        include_domain_list (bool):
            Whether to include the domain list.
    """

    include_va_query: bool = proto.Field(
        proto.BOOL,
        number=1,
    )
    include_nested_va_query: bool = proto.Field(
        proto.BOOL,
        number=2,
    )
    include_human_interpretation: bool = proto.Field(
        proto.BOOL,
        number=3,
    )
    include_aqua_debug_response: bool = proto.Field(
        proto.BOOL,
        number=4,
    )
    time_override: int = proto.Field(
        proto.INT64,
        number=5,
    )
    is_internal_google_user: bool = proto.Field(
        proto.BOOL,
        number=6,
    )
    ignore_cache: bool = proto.Field(
        proto.BOOL,
        number=7,
    )
    include_search_entities_rpc: bool = proto.Field(
        proto.BOOL,
        number=8,
    )
    include_list_column_annotations_rpc: bool = proto.Field(
        proto.BOOL,
        number=9,
    )
    include_virtual_analyst_entities: bool = proto.Field(
        proto.BOOL,
        number=10,
    )
    include_table_list: bool = proto.Field(
        proto.BOOL,
        number=11,
    )
    include_domain_list: bool = proto.Field(
        proto.BOOL,
        number=12,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
