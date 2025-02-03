import unittest
from test_switch_language import TestWikiEdit

def run_unittests(report_file):
    """
    Выполняет юнит-тесты с использованием unittest и записывает результаты в файл отчета.
    
    Аргументы:
        report_file (file-like object): Файл, в который будет записан отчет о выполнении тестов.
        
    Возвращает:
        result (unittest.result.TestResult): Результат выполнения тестов.
    """
    # Создаем тестовый набор и запускаем его
    suite = unittest.TestLoader().loadTestsFromTestCase(TestWikiEdit)
    runner = unittest.TextTestRunner(stream=report_file, verbosity=2)
    result = runner.run(suite)
    return result

if __name__ == '__main__':
    with open("test_report.txt", "w", encoding="utf-8") as report_file:
        report_file.write("=== Юнит-тесты ===\n")
        run_unittests(report_file)