from ultralytics import YOLO


def train(model, models_dir, conf):
    results = model.train(
        data=conf,
        imgsz=1280,
        epochs=10,
        batch=2,
        save_period=1,
        name=models_dir,
        device='mps'
    )
    return results


def val(model):
    metrics = model.val(
        data=conf,
        imgsz=1280,
        device='mps'
    )
    metrics.box.map
    metrics.box.map50
    metrics.box.map75
    metrics.box.maps


def predictor(model, models_dir):
    model.predict(
        source='/Users/alina/PycharmProjects/obj_detection/datasets/traffic_sign/yolo_format/valid/images',
        imgsz=1280,
        epochs=1,
        batch=2,
        name=models_dir,
        save=True
    )


def main(path_model, models_dir, conf):
    model = YOLO(path_model)
    train(model, models_dir, conf)
    val(model)


if __name__ == "__main__":
    path_model = '/model/best.pt'
    models_dir = '/model/model_v_russian_traffic_s'
    conf = '/Users/alina/PycharmProjects/obj_detection/conf/russian_trafic_signs.yaml'
    main()


