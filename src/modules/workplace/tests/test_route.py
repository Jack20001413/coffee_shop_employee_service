import unittest.mock
import fastapi
import pytest
import sqlalchemy.exc

from workplace import main
from workplace.repository import context as db_context

from workplace.repository.model import Workplace
from workplace.dtos.workplace_response import WorkplaceResponseDto

workplace_prefix = "/workplaces"


@pytest.fixture
@unittest.mock.patch("workplace.routes.workplace.DBSession")
def mock_db_session(mock_db_session) -> unittest.mock.MagicMock:
    return mock_db_session


@pytest.fixture
def override_dependencies(mock_db_session):
    main.app.dependency_overrides[db_context.get_session] = lambda: mock_db_session
    yield
    main.app.dependency_overrides = {}


def test_list_workplace_route_return_empty_list(
    mock_db_session, test_client, override_dependencies
) -> None:
    # Arrange
    expected_workplaces = []
    override_dependencies
    mock_db_session.exec.return_value.all.return_value = expected_workplaces

    # Act
    actual_resp = test_client.get(f"{workplace_prefix}/")
    result_workplaces = actual_resp.json()

    # Assert
    assert actual_resp.status_code == fastapi.status.HTTP_200_OK
    assert len(result_workplaces) == 0
    assert result_workplaces == expected_workplaces


def test_list_workspaces_route_return_workplace_list(
    test_client, mock_db_session, override_dependencies
) -> None:
    # Arrange
    test_workplace = WorkplaceResponseDto(
        id=1, name="Ledon City", address="182 Hong Bang"
    )
    expected_workplaces = [test_workplace.model_dump()]
    override_dependencies
    mock_db_session.exec.return_value.all.return_value = expected_workplaces

    # Act
    actual_resp = test_client.get(f"{workplace_prefix}/")
    result_workplaces = actual_resp.json()

    # Assert
    assert actual_resp.status_code == fastapi.status.HTTP_200_OK
    assert len(result_workplaces) > 0
    assert result_workplaces == expected_workplaces


def test_get_workplace_route_return_workplace_info(
    mock_db_session, test_client, override_dependencies
) -> None:
    # Arrange
    test_workplace_id = 1
    test_workplace = WorkplaceResponseDto(
        id=test_workplace_id, name="Ledon City", address="182 Hong Bang"
    )
    expected_workplace = test_workplace.model_dump()
    override_dependencies
    mock_db_session.exec.return_value.first.return_value = expected_workplace

    # Act
    actual_resp = test_client.get(f"{workplace_prefix}/{test_workplace_id}")
    result_workplace = actual_resp.json()

    # Assert
    assert actual_resp.status_code == fastapi.status.HTTP_200_OK
    assert result_workplace == expected_workplace


def test_get_workplace_route_cannot_find_workplace(
    mock_db_session, test_client, override_dependencies
) -> None:
    # Arrange
    test_workplace_id = 12
    expected_workplace = None
    override_dependencies
    mock_db_session.exec.return_value.first.return_value = expected_workplace

    # Act
    actual_resp = test_client.get(f"{workplace_prefix}/{test_workplace_id}")

    # Assert
    assert actual_resp.status_code == fastapi.status.HTTP_404_NOT_FOUND


def test_create_workplace_route_can_create_workplace(
    mock_db_session, test_client, override_dependencies
):
    # breakpoint()
    # Arrange
    test_workplace = {"name": "Leon City", "address": "182 Hong Bang"}
    expected_resp = dict({"id": 1}, **test_workplace)

    # Act
    actual_resp = test_client.post(f"{workplace_prefix}/", json=expected_resp)
    result_workplace = actual_resp.json()

    # Assert
    assert actual_resp.status_code == fastapi.status.HTTP_201_CREATED
    assert result_workplace == expected_resp

    mock_db_session.add.assert_called_once()


def test_patch_workplace_route_can_update_workplace(
    mock_db_session, test_client, override_dependencies
) -> None:
    # Arrange
    test_workplace_id = 1
    test_workplace = {"name": "Leon City", "address": "275 Hong Bang"}
    mock_current_workplace = Workplace(
        id=test_workplace_id, name="Leon City", address="275 Hong Bang"
    )
    mock_db_session.exec.return_value.first.return_value = mock_current_workplace

    # Act
    actual_resp = test_client.patch(
        f"{workplace_prefix}/{test_workplace_id}", json=test_workplace
    )

    # Assert
    assert actual_resp.status_code == fastapi.status.HTTP_204_NO_CONTENT

    mock_db_session.add.assert_called_once_with(mock_current_workplace)
    mock_db_session.commit.assert_called_once()


def test_patch_workplace_route_cannot_find_workplace(
    mock_db_session, test_client, override_dependencies
) -> None:
    # Arrange
    test_workplace_id = 1
    test_workplace = {"name": "Leon City", "address": "275 Hong Bang"}
    mock_db_session.exec.return_value.first.return_value = None

    # Act
    actual_resp = test_client.patch(
        f"{workplace_prefix}/{test_workplace_id}", json=test_workplace
    )

    # Assert
    assert actual_resp.status_code == fastapi.status.HTTP_404_NOT_FOUND

    mock_db_session.exec.assert_called_once()


def test_delete_workplace_route_can_delete_workplace(
    mock_db_session, test_client, override_dependencies
) -> None:
    # Arrange
    test_workplace_id = 1
    mock_current_workplace = Workplace(
        id=test_workplace_id, name="Leon City", address="275 Hong Bang"
    )
    mock_db_session.exec.return_value.one.return_value = mock_current_workplace

    # Act
    actual_resp = test_client.delete(f"{workplace_prefix}/{test_workplace_id}")

    # Assert
    assert actual_resp.status_code == fastapi.status.HTTP_204_NO_CONTENT

    mock_db_session.delete.assert_called_once_with(mock_current_workplace)
    mock_db_session.commit.assert_called_once()


def test_delete_workplace_route_cannot_find_workplace(
    mock_db_session, test_client, override_dependencies
) -> None:
    # Arrange
    test_workplace_id = 1
    mock_db_session.exec.return_value.one.side_effect = sqlalchemy.exc.NoResultFound

    # Act
    actual_resp = test_client.delete(f"{workplace_prefix}/{test_workplace_id}")

    # Assert
    assert actual_resp.status_code == fastapi.status.HTTP_404_NOT_FOUND

    mock_db_session.exec.assert_called_once()
