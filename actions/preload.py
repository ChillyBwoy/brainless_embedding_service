from app.dependencies import (
    _get_embedding_model,
    _get_prediction_model,
    _get_tokenizer,
    get_settings,
)


def main():
    settings = get_settings()
    _get_embedding_model(settings)
    _get_tokenizer(settings)
    _get_prediction_model(settings)


if __name__ == "__main__":
    main()
