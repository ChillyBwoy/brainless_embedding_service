from app.dependencies import _get_embedding_model, get_settings


def main():
    settings = get_settings()
    _get_embedding_model(settings)


if __name__ == "__main__":
    main()
