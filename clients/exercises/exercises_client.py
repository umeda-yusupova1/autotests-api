from clients.api_client import APIClient
from httpx import Response, QueryParams
from typing import TypedDict


class CreateExerciseRequestDict(TypedDict):
    """
    Описание структуры запроса на создание нового задания.
    """
    title: str
    courseId: str
    maxScore: int | None
    minScore: int | None
    orderIndex: int
    description: str
    estimatedTime: str | None


class UpdateExerciseRequestDict(TypedDict):
    """
    Описание структуры запроса на обновление задания.
    """
    title: str | None
    maxScore: int | None
    minScore: int | None
    orderIndex: int | None
    description: str | None
    estimatedTime: str | None


class ExercisesClient(APIClient):
    """
    Клиент для работы с /api/v1/exercises
    """

    def get_exercises_api(self, course_id: QueryParams) -> Response:
        """
        Метод получения списка заданий для определенного курса по идентификатору.

        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.get("/api/v1/exercises", params=course_id)

    def get_exercise_api(self, exercise_id: str) -> Response:
        """
        Метод получения информации о задании по UUID.

        :param exercise_id: Идентификатор задания.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.get(f"/api/v1/exercises/{exercise_id}")

    def create_exercise_api(self, request: CreateExerciseRequestDict) -> Response:
        """
        Метод выполняет создание нового задания.

        :param request: Словарь с title, courseId, maxScore, minScore, orderIndex, description, estimatedTime.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.post("/api/v1/exercises", json=request)

    def update_exercise_api(self, exercise_id: str, request: UpdateExerciseRequestDict) -> Response:
        """
        Метод обновления задания по идентификатору.

        :param exercise_id: Идентификатор задания.
        :param request: Словарь с title, courseId, maxScore, minScore, orderIndex, description, estimatedTime.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.patch(f"/api/v1/exercises/{exercise_id}", json=request)

    def delete_exercise_api(self, exercise_id: str) -> Response:
        """
        Метод удаления задания по идентификатору.

        :param exercise_id: Идентификатор задания.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.delete(f"/api/v1/exercises/{exercise_id}")
