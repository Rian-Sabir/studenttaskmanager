
import unittest
import task_manager


class TestTaskManager(unittest.TestCase):

    def setUp(self):
        task_manager.tasks.clear()
        task_manager.next_id = 1

    def test_add_task(self):
        task_manager.add_task("Complete assignment")

        self.assertEqual(len(task_manager.tasks), 2)
        self.assertEqual(
            task_manager.tasks[0]["title"],
            "Complete assignment"
        )
        self.assertFalse(task_manager.tasks[0]["completed"])

    def test_complete_task(self):
        task_manager.add_task("Study Git")

        task_manager.complete_task(1)

        self.assertTrue(task_manager.tasks[0]["completed"])

    def test_delete_task(self):
        task_manager.add_task("Submit project")

        task_manager.delete_task(1)

        self.assertEqual(len(task_manager.tasks), 0)


if __name__ == "__main__":
    unittest.main()
