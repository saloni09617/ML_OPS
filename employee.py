from abc import ABC, abstractmethod

# Base Employee class
class Employee(ABC):
    def __init__(self, emp_id, name, role):
        self.emp_id = emp_id
        self.name = name
        self.role = role

    @abstractmethod
    def work(self):
        pass


# ML Model class
class MLModel:
    def __init__(self, model_name):
        self.model_name = model_name
        self.trained = False

    def train(self):
        self.trained = True
        print(f"Model '{self.model_name}' trained successfully.")

    def evaluate(self):
        if self.trained:
            print(f"Model '{self.model_name}' evaluation completed.")
        else:
            print("Train the model first.")


# MLOps Engineer class
class MLOpsEngineer(Employee):
    def __init__(self, emp_id, name):
        super().__init__(emp_id, name, "MLOps Engineer")

    def build_pipeline(self):
        print("Building ML pipeline...")

    def deploy_model(self, model):
        if model.trained:
            print(f"Deploying model '{model.model_name}' to production.")
        else:
            print("Cannot deploy untrained model.")

    def monitor_model(self):
        print("Monitoring model performance and data drift.")

    def work(self):
        print(f"{self.name} is managing end-to-end ML lifecycle.")


# Main Execution
if __name__ == "__main__":
    emp = MLOpsEngineer(101, "Saloni")
    model = MLModel("Churn_Prediction_Model")

    emp.work()
    emp.build_pipeline()
    model.train()
    model.evaluate()
    emp.deploy_model(model)
    emp.monitor_model()
