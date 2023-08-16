1/ Bài nộp bao gồm:
    + 2 folder static và templates : cho front-end
    + 2 file .py predict và app : cho back-end
    + 1 file .ipynd : để train và tham chiếu mô hình phân loại dog và cat
    + 1 file best_score.pth là checkpoint của mô hình,1 file best_score.json chứa các thông tin của checkpoint
    + 1 folder mẫu bộ dữ liệu classify_data

2/ Một số thông tin về mô hình phân loại ảnh:
    - Mô hình được chọn là VGG16 , có đầu ra gồm 2 class dog(0) và cat(1) . Mô hình VGG16 được pretrained trên tập ImageNet
    - Thông số trainning: Batchsize = 16 , hàm tối ưu Adam , sử dụng Cross Entropy Loss , độ chính xác Top1 Accuracy
    - Bộ dữ liệu bao gồm 3 bộ : Đào tạo (24000 ảnh) , Đánh giá (1000 ảnh) , Thực nghiệm (12500 ảnh).
    - Ảnh được train trong 5 epoch , độ chính xác Top1 Accuracy cao nhất tại epoch 3 = 0.981 cho tập val bao gồm 1000 ảnh


3/ Kiến trúc của các folder bộ dữ liệu như sau:

                        classify_data
                                train
                                    cat.1.jpg
                                    cat.2.jpg
                                    cat.3.jpg
                                    ...
                                    cat.n.jpg
                                
                                val
                                    dog.1.jpg
                                    dog.2.jpg
                                    ...
                                    cat.n.jpg
                                
                                test
                                    1.jpg
                                    2.jpg
                                    3.jpg


--> tập train và tập val tên của đường dẫn ảnh phải có label trong đó --> ví dụ ảnh là dog thì tên phải là dog.x.jpg , ảnh là cat thì tên phải là cat.x.jpg
--> tập test có thể tên bất kì
--> trong các foldert train,val,test chỉ có ảnh , không có file khác ngoài ảnh  và các file ảnh phải có đuôi .jpg hoặc .png



5/	 - Để đào tạo thử trên bộ dữ liệu tự có:
    Thiết kế folder bộ dữ liệu tương tự như kiến trúc trên
    Chạy file ipydn từ đầu đến mục RUN , truyền vào các thông số config mong muốn

	- Để inference ảnh:
    Chạy file ipydn mục Infenrence và Feed a Img_Path:
    Truyền vào thông số config đường dẫn checkpoint và đường dẫn ảnh img_path 

	- Để chạy WebApp local sử dụng framework Flask:
    Chạy file app.py


6/ Các thông số config:
    cfg = {
    'SEED': 42,  # cho seeding

    'DATASET':
    {    
        'train_datadir': '/kaggle/input/qqqqqqq/classfy_data/train', # đường dẫn tập train
        'val_datadir' : '/kaggle/input/qqqqqqq/classfy_data/val',  # đường dẫn tập val
        'test_datadir': '/kaggle/input/qqqqqqq/classfy_data/test1', # đường dẫn tập test
        'image_size': 512  # kích thước ảnh đầu vào của mạng
    },
    
    'DATALOADER':
    {
        'batch_size': 16, 
        'num_workers': 0
    },
    
    'NETWORK':
    {
        'use_pretrained': True # có pretrained cho mạng hay không
    },

    'TRAIN':
    {
        'num_epochs': 5,  # tổng số epoch đào tạo
    },

    'OPTIMIZER': # tối ưu cho adam
    {
        'optim_name': 'adam',
        'lr': 0.0001,
        'weight_decay': 0.00001,
        'momentum': 0.9
    },
    'LOG':
    {
        'eval_interval': 1  # sau bao nhiêu epoch thì đánh giá 1 lần
    },
    'RESULT':
    {
        'savedir': 'saving'
    },

    'checkpoint' : 'best_score.pth', # đường dẫn cho file checkpoint
    'img_path': 'classify_data/test1/3.jpg # đường dẫn để tham chiếu ảnh
}

Download checkpoint best_score.pth
https://drive.google.com/file/d/1STg3QxXwuOHEmmole1aPMmD9XaWen_wO/view?usp=sharing
