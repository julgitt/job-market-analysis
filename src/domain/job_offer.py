class JobOffer:
    def __init__(
        self,
        slug: str,
        company_name: str,
        title: str,
        description: str,
        remote: bool,
        url: str,
        tags: list[str],
        job_types: list[str],
        location: str,
        created_at: int,
    ):
        self.slug = slug
        self.company_name = company_name
        self.title = title
        self.description = description
        self.remote = remote
        self.url = url
        self.tags = tags
        self.job_types = job_types
        self.location = location
        self.created_at = created_at

    def has_required_fields(self) -> bool:
        if not isinstance(self.slug, str) or not self.slug.strip():
            return False

        if not isinstance(self.company_name, str) or not self.company_name.strip():
            return False

        if not isinstance(self.title, str) or not self.title.strip():
            return False

        return True
