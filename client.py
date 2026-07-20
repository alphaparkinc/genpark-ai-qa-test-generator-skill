class AiQaTestGeneratorClient:
    def generate_tests(self, feature_description: str, test_framework: str) -> dict:
        fw = test_framework.lower()
        prefix = "test_" if "pytest" in fw else "it("
        suffix = "" if "pytest" in fw else ")"
        words = [w.strip(".,!?") for w in feature_description.split() if len(w) > 4]
        entity = words[0] if words else "feature"
        test_cases = [
            f"{prefix}should_render_{entity}_successfully{suffix}",
            f"{prefix}should_validate_required_fields_for_{entity}{suffix}",
            f"{prefix}should_handle_{entity}_api_error_gracefully{suffix}",
            f"{prefix}should_restrict_unauthorized_{entity}_access{suffix}",
            f"{prefix}should_complete_{entity}_happy_path_end_to_end{suffix}"
        ]
        coverage_areas = ["Rendering", "Validation", "Error handling", "Auth & access control", "E2E flow"]
        return {"test_cases": test_cases, "coverage_areas": coverage_areas}
