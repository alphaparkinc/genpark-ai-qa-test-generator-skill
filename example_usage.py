from client import AiQaTestGeneratorClient
client = AiQaTestGeneratorClient()
result = client.generate_tests(
    feature_description="User login with email and password with 2FA support",
    test_framework="pytest"
)
print(f"Coverage areas: {result['coverage_areas']}")
print("Generated test cases:")
for tc in result["test_cases"]:
    print(f"  def {tc}(): ...")
