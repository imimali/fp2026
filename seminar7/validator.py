from seminar7.domain import Cat

class ValidationError(Exception):
    pass

class CatValidator():
    @staticmethod
    def validate(cat:Cat):
        errors = []
        if not cat.get_name():
            errors.append("Name cannot be void")
        if not cat.get_race():
            errors.append("Race cannot be empty")
        if not 0 < cat.get_weight() < 10_000_000:
            errors.append("Weight must be within bounds")
        if errors:
            raise ValidationError(",".join(errors))





