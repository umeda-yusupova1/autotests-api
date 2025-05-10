from clients.errors_schema import InternalErrorResponseSchema
from clients.exercises.exercises_schema import (CreateExerciseRequestSchema,
                                                ExerciseResponseSchema,
                                                ExerciseSchema,
                                                UpdateExerciseRequestSchema)
from tools.assertions.base import assert_equal
from tools.assertions.errors import assert_internal_error_response


def assert_create_exercise_response(
        request: CreateExerciseRequestSchema,
        response: ExerciseResponseSchema
):
    """
    Проверяет, что ответ на создание задания соответствует запросу.

    :param request: Исходный запрос на создание задания.
    :param response: Ответ API с данными задания.
    :raises AssertionError: Если хотя бы одно поле не совпадает.
    """
    assert_equal(request.title, response.exercise.title, "title")
    assert_equal(request.course_id, response.exercise.course_id, "course_id")
    assert_equal(request.max_score, response.exercise.max_score, "max_score")
    assert_equal(request.min_score, response.exercise.min_score, "min_score")
    assert_equal(request.order_index, response.exercise.order_index, "order_index")
    assert_equal(request.description, response.exercise.description, "description")
    assert_equal(request.estimated_time, response.exercise.estimated_time, "estimated_time")


def assert_exercise(actual: ExerciseSchema, expected: ExerciseSchema):
    """
    Проверяет, что фактические данные задания соответствуют ожидаемым.

    :param actual: Фактические данные задания.
    :param expected: Ожидаемые данные задания.
    :raises AssertionError: Если хотя бы одно поле не совпадает.
    """
    assert_equal(actual.id, expected.id, "id")
    assert_equal(actual.title, expected.title, "title")
    assert_equal(actual.course_id, expected.course_id, "course_id")
    assert_equal(actual.max_score, expected.max_score, "max_score")
    assert_equal(actual.min_score, expected.min_score, "min_score")
    assert_equal(actual.order_index, expected.order_index, "order_index")
    assert_equal(actual.description, expected.description, "description")
    assert_equal(actual.estimated_time, expected.estimated_time, "estimated_time")


def assert_get_exercise_response(
        get_exercise_response: ExerciseResponseSchema,
        create_exercise_responses: ExerciseResponseSchema
):
    """
    Проверяет, что ответ на получение задания соответствует ответу на его создание.

    :param get_exercise_response: Ответ API при запросе на получение задания.
    :param create_exercise_responses: Ответ API при создании задания.
    :raises AssertionError: Если данные пользователя не совпадают.
    """
    assert_exercise(get_exercise_response.exercise, create_exercise_responses.exercise)


def assert_update_exercise_response(
        request: UpdateExerciseRequestSchema,
        response: ExerciseResponseSchema
):
    """
    Проверяет, что ответ на обновление задания соответствует данным из запроса.

    :param request: Исходный запрос на обновление задания.
    :param response: Ответ API с обновленными данными задания.
    :raises AssertionError: Если хотя бы одно поле не совпадает.
    """
    if request.title is not None:
        assert_equal(response.exercise.title, request.title, "title")

    if request.max_score is not None:
        assert_equal(response.exercise.max_score, request.max_score, "max_score")

    if request.min_score is not None:
        assert_equal(response.exercise.min_score, request.min_score, "min_score")

    if request.order_index is not None:
        assert_equal(response.exercise.order_index, request.order_index, "order_index")

    if request.description is not None:
        assert_equal(response.exercise.description, request.description, "description")

    if request.estimated_time is not None:
        assert_equal(response.exercise.estimated_time, request.estimated_time, "estimated_time")


def assert_exercise_not_found_response(actual: InternalErrorResponseSchema):
    """
    Функция для проверки ошибки, возникающей при выполнении запроса к несуществующему заданию.

    :param actual: Фактический ответ.
    :raises AssertionError: Если фактический ответ не соответствует ошибке "Exercise not found"
    """
    expected = InternalErrorResponseSchema(details="Exercise not found")
    assert_internal_error_response(actual, expected)
