import pytest
import dataclasses

from src.domain.user.entities import User


class TestEntity:
    @pytest.mark.parametrize(
        "entity_class, dataset",
        (User, {"name": "이름"}),
    )
    def test_constructor(self, entity_class, dataset: dict):
        # given
        entity = entity_class.from_data(dataset)

        # when
        for key, criteria in dataset.items():
            target = getattr(entity, key)

            # then
            assert target == criteria

    @pytest.mark.parametrize(
        "entity_class, dataset",
        (User, {"name": "이름"}),
    )
    def test_should_be_frozen(self, entity_class, dataset: dict):
        with pytest.raises(dataclasses.FrozenInstanceError):
            # Given
            entity = entity_class.from_data(dataset)

            # when
            entity.id = "11"

            # Then
