from domain.item_classifier import get_rule_for

class UpdateInventoryUseCase:
    def execute(self, items) -> None:
        for item in items:
            rule = get_rule_for(item.name)
            rule.update(item)
