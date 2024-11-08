import joblib
import onnxmltools
from skl2onnx import convert_sklearn
from skl2onnx.common.data_types import FloatTensorType

def convert_to_onnx():
    # Load the trained model
    model = joblib.load("models/virality_model.pkl")

    # Define input type for conversion
    initial_type = [('float_input', FloatTensorType([None, len(model.feature_importances_)]))]
    onnx_model = convert_sklearn(model, initial_types=initial_type)

    # Save ONNX model
    with open("models/virality_model.onnx", "wb") as f:
        f.write(onnx_model.SerializeToString())
    print("Virality model converted to ONNX and saved.")

if __name__ == "__main__":
    convert_to_onnx()
