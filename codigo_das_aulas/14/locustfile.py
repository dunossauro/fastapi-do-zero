from locust import HttpUser, task


class FastAPIUser(HttpUser):

    @task
    def read_users(self):
        self.client.get('/users/')
