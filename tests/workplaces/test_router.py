from unittest.mock import MagicMock, patch

from fastapi import Response, status
from sqlalchemy.exc import NoResultFound
import pytest

from src.main import app
from src.services.workplace import WorkplaceService


workplace_prefix = "/workplaces"


@pytest.fixture
@patch("app.routers.workplace.WorkplaceService")
def mock_workplace_service(mock_service) -> MagicMock:
    return mock_service


def test_list_workplaces_route_return_empty_list(
    mock_workplace_service, test_client
) -> None:
    # Arrange
    expected_resp = []
    app.dependency_overrides[WorkplaceService] = lambda: mock_workplace_service
    mock_workplace_service.get_workplaces.return_value = expected_resp

    # Act
    actual_resp: Response = test_client.get(f"{workplace_prefix}/")
    workplaces = actual_resp.json()

    # Assert
    assert actual_resp.status_code == status.HTTP_200_OK
    assert len(workplaces) == 0
    assert workplaces == expected_resp


def test_list_workspaces_route_return_workplace_list(
    mock_workplace_service, test_client
) -> None:
    # Arrange
    dump_workplace = {"id": 1, "name": "Ledon City", "address": "182 Hong Bang"}
    expected_resp = [dump_workplace]
    app.dependency_overrides[WorkplaceService] = lambda: mock_workplace_service
    mock_workplace_service.get_workplaces.return_value = expected_resp

    # Act
    actual_resp: Response = test_client.get(f"{workplace_prefix}/")
    workplaces = actual_resp.json()

    # Assert
    assert actual_resp.status_code == status.HTTP_200_OK
    assert len(workplaces) > 0
    assert workplaces == expected_resp


def test_get_workplace_route_return_workplace_info(
    mock_workplace_service, test_client
) -> None:
    # Arrange
    resource_id = 1
    expected_resp = {"id": 1, "name": "Leon City", "address": "275 Hong Bang"}
    app.dependency_overrides[WorkplaceService] = lambda: mock_workplace_service
    mock_workplace_service.get_workplace_by_id.return_value = expected_resp

    # Act
    actual_resp = test_client.get(f"{workplace_prefix}/{resource_id}")
    workplace = actual_resp.json()

    # Assert
    assert actual_resp.status_code == status.HTTP_200_OK
    assert workplace == expected_resp


def test_get_workplace_route_cannot_find_workplace(
    mock_workplace_service, test_client
) -> None:
    # Arrange
    resource_id = 12
    expected_resp = None
    app.dependency_overrides[WorkplaceService] = lambda: mock_workplace_service
    mock_workplace_service.get_workplace_by_id.return_value = expected_resp

    # Act
    actual_resp = test_client.get(f"{workplace_prefix}/{resource_id}")

    # Assert
    assert actual_resp.status_code == status.HTTP_404_NOT_FOUND


def test_create_workplace_route_can_create_workplace(
    mock_workplace_service, test_client
) -> None:
    # Arrange
    input_workplace = {"name": "Leon City", "address": "275 Hong Bang"}
    expected_resp = dict({"id": 1}, **input_workplace)
    app.dependency_overrides[WorkplaceService] = lambda: mock_workplace_service
    mock_workplace_service.create_workplace.return_value = expected_resp

    # Act
    actual_resp = test_client.post(f"{workplace_prefix}/", json=input_workplace)
    workplace = actual_resp.json()

    # Assert
    assert actual_resp.status_code == status.HTTP_201_CREATED
    mock_workplace_service.create_workplace.assert_called_once()
    assert workplace == expected_resp


def test_patch_workplace_route_can_update_workplace(
    mock_workplace_service, test_client
) -> None:
    # Arrange
    input_workplace_id = 1
    input_workplace = {"name": "Leon City", "address": "275 Hong Bang"}
    app.dependency_overrides[WorkplaceService] = lambda: mock_workplace_service
    mock_workplace_service.update_workplace.return_value = None

    # Act
    actual_resp = test_client.patch(
        f"{workplace_prefix}/{input_workplace_id}", json=input_workplace
    )

    # Assert
    assert actual_resp.status_code == status.HTTP_204_NO_CONTENT
    mock_workplace_service.update_workplace.assert_called_once()


def test_patch_workplace_route_cannot_find_workplace(
    mock_workplace_service, test_client
) -> None:
    # Arrange
    input_workplace_id = 1
    input_workplace = {"name": "Leon City", "address": "275 Hong Bang"}
    app.dependency_overrides[WorkplaceService] = lambda: mock_workplace_service
    mock_workplace_service.update_workplace.side_effect = NoResultFound

    # Act
    actual_resp = test_client.patch(
        f"{workplace_prefix}/{input_workplace_id}", json=input_workplace
    )

    # Assert
    assert actual_resp.status_code == status.HTTP_404_NOT_FOUND

    mock_workplace_service.update_workplace.assert_called_once()


def test_delete_workplace_route_can_delete_workplace(
    mock_workplace_service, test_client
) -> None:
    # Arrange
    input_workplace_id = 1
    app.dependency_overrides[WorkplaceService] = lambda: mock_workplace_service
    mock_workplace_service.delete_workplace.return_value = None

    # Act
    actual_resp = test_client.delete(f"{workplace_prefix}/{input_workplace_id}")

    # Assert
    assert actual_resp.status_code == status.HTTP_204_NO_CONTENT

    mock_workplace_service.delete_workplace.assert_called_once()
    # No keyword argument is used in WorkplaceService.delete_workplace(), so assert_called_once_with(workplace_id=input_workplace_id) is NOT valid
    mock_workplace_service.delete_workplace.assert_called_once_with(input_workplace_id)


def test_delete_workplace_route_cannot_find_workplace(
    mock_workplace_service, test_client
) -> None:
    # Arrange
    input_workplace_id = 1
    app.dependency_overrides[WorkplaceService] = lambda: mock_workplace_service
    mock_workplace_service.delete_workplace.side_effect = NoResultFound

    # Act
    actual_resp = test_client.delete(f"{workplace_prefix}/{input_workplace_id}")

    # Assert
    assert actual_resp.status_code == status.HTTP_404_NOT_FOUND

    mock_workplace_service.delete_workplace.assert_called_once()
    mock_workplace_service.delete_workplace.assert_called_once_with(input_workplace_id)


def test_delete_workplace_route_cannot_delete_workplace(
    mock_workplace_service, test_client
):
    # Arrange
    input_workplace_id = 1
    app.dependency_overrides[WorkplaceService] = lambda: mock_workplace_service
    mock_workplace_service.delete_workplace.side_effect = Exception

    # Act
    actual_resp = test_client.delete(f"{workplace_prefix}/{input_workplace_id}")

    # Assert
    assert actual_resp.status_code == status.HTTP_500_INTERNAL_SERVER_ERROR

    mock_workplace_service.delete_workplace.assert_called_once()
    mock_workplace_service.delete_workplace.assert_called_once_with(input_workplace_id)
