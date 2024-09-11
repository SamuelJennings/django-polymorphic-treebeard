from django.apps import apps


def resolve_model_reference(model, current_class):
    """
    Resolves the model reference in the same way as the `to` parameter on a ForeignKey.
    - If the model is a string, it can be "self", an app model string "app_label.ModelName", or "ModelName".
    - If the model is already a model class, it returns it directly.
    """
    if isinstance(model, str):
        if model == "self":
            return current_class
        try:
            # Check if it's an app model string like "app_label.ModelName"
            return apps.get_model(model)
        except ValueError:
            # If it's a model string within the same app (e.g., "ModelName")
            return apps.get_model(current_class._meta.app_label, model)
    return model
