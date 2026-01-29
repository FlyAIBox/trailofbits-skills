"""Tests for user registration endpoint."""

import pytest
from fastapi.testclient import TestClient


def test_register_success(client: TestClient) -> None:
    """Test successful user registration."""
    response = client.post(
        "/register",
        json={
            "username": "alice",
            "email": "alice@example.com",
            "password": "SecureP@ssw0rd123",
        },
    )

    assert response.status_code == 201
    data = response.json()
    assert "user_id" in data
    assert "token" in data
    assert isinstance(data["user_id"], int)
    assert isinstance(data["token"], str)


def test_register_duplicate_username(client: TestClient) -> None:
    """Test registration with duplicate username."""
    # First registration
    client.post(
        "/register",
        json={
            "username": "bob",
            "email": "bob@example.com",
            "password": "SecureP@ssw0rd123",
        },
    )

    # Second registration with same username
    response = client.post(
        "/register",
        json={
            "username": "bob",
            "email": "different@example.com",
            "password": "SecureP@ssw0rd123",
        },
    )

    assert response.status_code == 400
    assert "already exists" in response.json()["detail"]


def test_register_duplicate_email(client: TestClient) -> None:
    """Test registration with duplicate email."""
    # First registration
    client.post(
        "/register",
        json={
            "username": "charlie",
            "email": "charlie@example.com",
            "password": "SecureP@ssw0rd123",
        },
    )

    # Second registration with same email
    response = client.post(
        "/register",
        json={
            "username": "different",
            "email": "charlie@example.com",
            "password": "SecureP@ssw0rd123",
        },
    )

    assert response.status_code == 400
    assert "already exists" in response.json()["detail"]


def test_register_invalid_email(client: TestClient) -> None:
    """Test registration with invalid email format."""
    response = client.post(
        "/register",
        json={
            "username": "dave",
            "email": "not-an-email",
            "password": "SecureP@ssw0rd123",
        },
    )

    assert response.status_code == 422


def test_register_weak_password(client: TestClient) -> None:
    """Test registration with weak password (no uppercase)."""
    response = client.post(
        "/register",
        json={
            "username": "eve",
            "email": "eve@example.com",
            "password": "weakpassword123!",
        },
    )

    assert response.status_code == 422


def test_register_short_password(client: TestClient) -> None:
    """Test registration with password too short."""
    response = client.post(
        "/register",
        json={
            "username": "frank",
            "email": "frank@example.com",
            "password": "Short1!",
        },
    )

    assert response.status_code == 422


def test_register_invalid_username(client: TestClient) -> None:
    """Test registration with invalid username (contains spaces)."""
    response = client.post(
        "/register",
        json={
            "username": "invalid username",
            "email": "test@example.com",
            "password": "SecureP@ssw0rd123",
        },
    )

    assert response.status_code == 422


def test_register_short_username(client: TestClient) -> None:
    """Test registration with username too short."""
    response = client.post(
        "/register",
        json={
            "username": "ab",
            "email": "test@example.com",
            "password": "SecureP@ssw0rd123",
        },
    )

    assert response.status_code == 422


def test_health_check(client: TestClient) -> None:
    """Test health check endpoint."""
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}

