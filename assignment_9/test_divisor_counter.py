import pytest
from divisor_counter import DivisorEqualityAnalyzer


class TestFactorComputation:

    @pytest.fixture
    def analyzer(self):
        return DivisorEqualityAnalyzer()

    def test_divisor_count_for_unit(self, analyzer):
        assert analyzer.get_total_divisors(1) == 1

    def test_divisor_count_for_primes(self, analyzer):
        assert analyzer.get_total_divisors(2) == 2
        assert analyzer.get_total_divisors(3) == 2
        assert analyzer.get_total_divisors(7) == 2

    def test_divisor_count_for_composites(self, analyzer):
        assert analyzer.get_total_divisors(4) == 3
        assert analyzer.get_total_divisors(6) == 4
        assert analyzer.get_total_divisors(12) == 6
        assert analyzer.get_total_divisors(14) == 4
        assert analyzer.get_total_divisors(15) == 4

    def test_invalid_input_raises_error(self, analyzer):
        with pytest.raises(ValueError):
            analyzer.get_total_divisors(0)
        with pytest.raises(ValueError):
            analyzer.get_total_divisors(-10)


class TestEqualityScanning:

    @pytest.fixture
    def analyzer(self):
        return DivisorEqualityAnalyzer()

    def test_scenario_k15_returns_two(self, analyzer):
        assert analyzer.count_consecutive_matches(15) == 2

    def test_minimal_intervals(self, analyzer):
        with pytest.raises(ValueError):
            analyzer.count_consecutive_matches(1)
        with pytest.raises(ValueError):
            analyzer.count_consecutive_matches(2)
        assert analyzer.count_consecutive_matches(3) == 1

    def test_input_validation(self, analyzer):
        with pytest.raises(TypeError):
            analyzer.count_consecutive_matches("15")
        with pytest.raises(ValueError):
            analyzer.count_consecutive_matches(0)


class TestFullAnalysisWorkflow:

    @pytest.fixture
    def analyzer(self):
        return DivisorEqualityAnalyzer()

    def test_standard_execution_flow(self, analyzer):
        test_cases = [15, 3]
        expected_results = [2, 1]
        assert analyzer.run_analysis(test_cases) == expected_results

    def test_empty_suite(self, analyzer):
        assert analyzer.run_analysis([]) == []

    def test_workflow_error_handling(self, analyzer):
        with pytest.raises(TypeError):
            analyzer.run_analysis(None)
        with pytest.raises(ValueError):
            analyzer.run_analysis([15, -1])


class TestProblemDemonstration:

    @pytest.fixture
    def analyzer(self):
        return DivisorEqualityAnalyzer()

    def test_n2_and_n3_match(self, analyzer):
        assert analyzer.get_total_divisors(2) == analyzer.get_total_divisors(3)

    def test_n14_and_n15_match(self, analyzer):
        assert analyzer.get_total_divisors(14) == analyzer.get_total_divisors(15)

    def test_n3_and_n4_mismatch(self, analyzer):
        assert analyzer.get_total_divisors(3) != analyzer.get_total_divisors(4)
