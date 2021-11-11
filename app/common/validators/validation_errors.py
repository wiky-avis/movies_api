from typing import List


def validation_errors_to_dict(errors: dict) -> List[dict]:
    validation_errors = []
    for field_name, field_errors in errors.items():
        for err in field_errors:
            validation_errors.append({'loc': ['query', field_name], 'msg': err})
    return validation_errors
