{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "f34634f8-df5e-40ac-bedc-61807863200b",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'cuda'"
      ]
     },
     "execution_count": 1,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "import pandas as pd\n",
    "import numpy as np\n",
    "import torch\n",
    "from tqdm.auto import tqdm\n",
    "import random\n",
    "import os\n",
    "\n",
    "def reset_seeds(seed):\n",
    "    random.seed(seed)\n",
    "    os.environ['PYTHONHASHSEED'] = str(seed)\n",
    "    np.random.seed(seed)\n",
    "    torch.manual_seed(seed)\n",
    "    torch.cuda.manual_seed(seed)\n",
    "    torch.backends.cudnn.deterministic = True\n",
    "\n",
    "device = 'cuda' if torch.cuda.is_available() else 'cpu'\n",
    "device"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "d51b48e3-0b3a-4d75-b427-cdb9e000bb1a",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(14767, 9)"
      ]
     },
     "execution_count": 2,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "buying_concat = pd.read_excel('buying_concat.xlsx')\n",
    "buying_concat.shape"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "b85e8f47-7f22-4b5c-b031-ac61f68b98e8",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(44356, 7)"
      ]
     },
     "execution_count": 3,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "test_ft = pd.read_excel('review_drop_dup.xlsx')\n",
    "test_ft.shape"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "4cf9e62f-5542-442b-b455-4f11fd395fa7",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(7193, 24)"
      ]
     },
     "execution_count": 4,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "train_ft = pd.read_excel('zigzag_clothes.xlsx')\n",
    "train_ft.shape"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "96b8eac3-68da-4bbe-96a5-713e3b2e8924",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(7193,)"
      ]
     },
     "execution_count": 5,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "train_arr = train_ft['리뷰'].to_numpy()\n",
    "train_arr.shape"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "59a14100-2c86-4720-85ae-397a9f77067c",
   "metadata": {},
   "outputs": [],
   "source": [
    "from transformers import AutoTokenizer, AutoModel"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "c1cbe13c-0576-4aa8-8b75-6d60c16bc8be",
   "metadata": {},
   "outputs": [],
   "source": [
    "model_name = 'kykim/bert-kor-base'"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "649e7b0b-44b9-492e-8738-7b97344d9ddb",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "/home/lab01/.local/lib/python3.10/site-packages/torch/_utils.py:776: UserWarning: TypedStorage is deprecated. It will be removed in the future and UntypedStorage will be the only storage class. This should only matter to you if you are using storages directly.  To access UntypedStorage directly, use tensor.untyped_storage() instead of tensor.storage()\n",
      "  return self.fget.__get__(instance, owner)()\n"
     ]
    }
   ],
   "source": [
    "model = AutoModel.from_pretrained(model_name)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "eb9d4534-07f7-4cd2-809d-440e92100589",
   "metadata": {},
   "outputs": [],
   "source": [
    "tokenizer = AutoTokenizer.from_pretrained(model_name)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "1bea5a3f-6c0f-47ef-88ed-b23acbbe7491",
   "metadata": {},
   "source": [
    "# 클래스 정리"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "3d45731b-e20b-4ff0-85d8-9b5d5e7e39cb",
   "metadata": {},
   "outputs": [],
   "source": [
    "class ReviewDataset(torch.utils.data.Dataset):\n",
    "    def __init__(self, tokenizer, x, y=None):\n",
    "        self.tokenizer = tokenizer\n",
    "        self.x = x\n",
    "        self.y = y\n",
    "    def __len__(self):\n",
    "        return len(self.x)\n",
    "    def __getitem__(self, idx):\n",
    "        item = {}\n",
    "        item[\"x\"] = self.get_tokenizer(self.x[idx])\n",
    "        if self.y is not None:\n",
    "            item[\"y\"] = torch.Tensor(self.y[idx])\n",
    "        return item\n",
    "    def get_tokenizer(self, text):\n",
    "        x = self.tokenizer(text, padding=\"max_length\", truncation=True)\n",
    "        for k, v in x.items():\n",
    "            x[k] = torch.tensor(v)\n",
    "        return x"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "b36fe296-2a38-4c56-9f2a-419c46025d70",
   "metadata": {},
   "outputs": [],
   "source": [
    "# 키워드 포함 여부에 대한 class\n",
    "class Net(torch.nn.Module):\n",
    "    def __init__(self, model_name):\n",
    "        super().__init__()\n",
    "        self.pre_model = AutoModel.from_pretrained(model_name)\n",
    "        self.fc_out = torch.nn.Linear( self.pre_model.config.hidden_size, 7)\n",
    "\n",
    "    def forward(self, x):\n",
    "        x = self.pre_model(**x)\n",
    "        # x[0]: 모든 시점의 히든출력 batch, seq, features\n",
    "        # x[1]: CLS 토큰의 히든출력 batch, features\n",
    "        return self.fc_out(x[1])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "042acbab-12d1-4b36-83ae-6235a703f9ac",
   "metadata": {},
   "outputs": [],
   "source": [
    "# 키워드별로 긍/부정을 예측하는 class\n",
    "class Net_emotion(torch.nn.Module):\n",
    "    def __init__(self, model_name):\n",
    "        super().__init__()\n",
    "        self.pre_model = AutoModel.from_pretrained(model_name)\n",
    "        self.fc_out = torch.nn.Linear( self.pre_model.config.hidden_size, 1)\n",
    "\n",
    "    def forward(self, x):\n",
    "        x = self.pre_model(**x)\n",
    "        # x[0]: 모든 시점의 히든출력 batch, seq, features\n",
    "        # x[1]: CLS 토큰의 히든출력 batch, features\n",
    "        return self.fc_out(x[1])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "954be317-8e82-4115-ae29-1d3af88b9af2",
   "metadata": {},
   "outputs": [],
   "source": [
    "# 모델의 가중치를 받아온 뒤 예측을 진행\n",
    "@torch.no_grad()\n",
    "def test_loop(dataloader, model, device):\n",
    "    pred_list = []\n",
    "    act_func = torch.nn.Sigmoid()\n",
    "    model.eval() # 평가 모드\n",
    "    for batch in tqdm(dataloader):\n",
    "        pred = model( batch[\"x\"].to(device) )\n",
    "        pred = act_func(pred) # logit 값을 확률로 변환\n",
    "        pred = pred.to(\"cpu\").numpy() # cpu 이동후 ndarray 로변환\n",
    "        pred_list.append(pred)\n",
    "\n",
    "    pred = np.concatenate(pred_list)\n",
    "    return pred"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "bceba2f3-21a7-4510-9102-a1578a91951c",
   "metadata": {},
   "outputs": [],
   "source": [
    "# 모델의 가중치를 받아온 뒤 예측을 진행\n",
    "@torch.no_grad()\n",
    "def test_loop_emotion(dataloader, model, device):\n",
    "    pred_list = []\n",
    "    act_func = torch.nn.Sigmoid()\n",
    "    model.eval() # 평가 모드\n",
    "    for batch in dataloader:\n",
    "        pred = model( batch[\"x\"].to(device) )\n",
    "        pred = act_func(pred) # logit 값을 확률로 변환\n",
    "        pred = pred.to(\"cpu\").numpy() # cpu 이동후 ndarray 로변환\n",
    "        pred_list.append(pred)\n",
    "\n",
    "    pred = np.concatenate(pred_list)\n",
    "    return pred"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "fb793b44-8cfd-432d-affb-cfde633c9265",
   "metadata": {},
   "source": [
    "# 키워드 존재 여부 판별 & 키워드별 긍/부정 예측 모델 "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "17bc3522-5458-49d1-8b7c-45e8ce8c56e0",
   "metadata": {},
   "outputs": [],
   "source": [
    "def Review_classification(review):                       \n",
    "    if isinstance(review,pd.Series): # review가 Series의 형태와 그렇지 않은 경우로 나뉨. 그렇지 않은 경우에는 list의 형식을 전달\n",
    "        test_arr = review.to_numpy()\n",
    "    else:\n",
    "        test_arr = pd.Series(review).to_numpy()\n",
    "        \n",
    "    test_dt = ReviewDataset(tokenizer,test_arr)\n",
    "    test_dl = torch.utils.data.DataLoader(test_dt,batch_size = 8,shuffle = False)\n",
    "    \n",
    "    pred_list = []\n",
    "\n",
    "    model = Net(model_name).to(device)\n",
    "    state_dict = torch.load(\"model_0.pth\")\n",
    "    model.load_state_dict(state_dict)\n",
    "    \n",
    "    pred = test_loop(test_dl, model, device) \n",
    "    pred_list.append(pred)\n",
    "    pred = np.mean(pred_list, axis=0)\n",
    "    pred = (pred > 0.5).astype(int)\n",
    "\n",
    "    model = Net_emotion(model_name).to(device)\n",
    "    state_dict_color = torch.load('color.pth')\n",
    "    state_dict_fit = torch.load('fit.pth')\n",
    "    state_dict_texture = torch.load('texture.pth')\n",
    "    state_dict_quality = torch.load('quality.pth')\n",
    "    state_dict_status = torch.load('status.pth')\n",
    "    state_dict_price = torch.load('price.pth')\n",
    "    state_dict_thickness = torch.load('thickness.pth')\n",
    "    \n",
    "    for i,v in tqdm(enumerate(pred),total = len(test_arr)): \n",
    "          if v[0] == 1: \n",
    "              test_dt = ReviewDataset(tokenizer,test_arr[i:i+1]) \n",
    "              test_dl = torch.utils.data.DataLoader(test_dt,batch_size = 8,shuffle = False)\n",
    "              \n",
    "              pred_list = []\n",
    "    \n",
    "              model.load_state_dict(state_dict_color)  \n",
    "              pred_color = test_loop_emotion(test_dl, model, device) \n",
    "              pred_list.append(pred_color)\n",
    "                  \n",
    "              pred_color = np.mean(pred_list, axis=0)\n",
    "              pred_color = (pred_color > 0.5).astype(int)\n",
    "                        \n",
    "              if pred_color[0] == 1:\n",
    "                  v[0] = 1\n",
    "              else:\n",
    "                  v[0] = -1\n",
    "\n",
    "          if v[1] == 1: \n",
    "              test_dt = ReviewDataset(tokenizer,test_arr[i:i+1]) \n",
    "              test_dl = torch.utils.data.DataLoader(test_dt,batch_size = 8,shuffle = False)\n",
    "              \n",
    "              pred_list = []\n",
    "    \n",
    "              model.load_state_dict(state_dict_fit)  \n",
    "              pred_fit = test_loop_emotion(test_dl, model, device) \n",
    "              pred_list.append(pred_fit)\n",
    "                  \n",
    "              pred_fit = np.mean(pred_list, axis=0)\n",
    "              pred_fit = (pred_fit > 0.5).astype(int)\n",
    "                        \n",
    "              if pred_fit[0] == 1:\n",
    "                  v[1] = 1\n",
    "              else:\n",
    "                  v[1] = -1\n",
    "\n",
    "          if v[2] == 1: \n",
    "              test_dt = ReviewDataset(tokenizer,test_arr[i:i+1]) \n",
    "              test_dl = torch.utils.data.DataLoader(test_dt,batch_size = 8,shuffle = False)\n",
    "              \n",
    "              pred_list = []\n",
    "    \n",
    "              model.load_state_dict(state_dict_texture)  \n",
    "              pred_texture = test_loop_emotion(test_dl, model, device) \n",
    "              pred_list.append(pred_texture)\n",
    "                  \n",
    "              pred_texture = np.mean(pred_list, axis=0)\n",
    "              pred_texture = (pred_texture > 0.5).astype(int)\n",
    "                        \n",
    "              if pred_texture[0] == 1:\n",
    "                  v[2] = 1\n",
    "              else:\n",
    "                  v[2] = -1\n",
    "\n",
    "          if v[3] == 1: \n",
    "              test_dt = ReviewDataset(tokenizer,test_arr[i:i+1]) \n",
    "              test_dl = torch.utils.data.DataLoader(test_dt,batch_size = 8,shuffle = False)\n",
    "              \n",
    "              pred_list = []\n",
    "    \n",
    "              model.load_state_dict(state_dict_quality)  \n",
    "              pred_quality = test_loop_emotion(test_dl, model, device) \n",
    "              pred_list.append(pred_quality)\n",
    "                  \n",
    "              pred_quality = np.mean(pred_list, axis=0)\n",
    "              pred_quality = (pred_quality > 0.5).astype(int)\n",
    "                        \n",
    "              if pred_quality[0] == 1:\n",
    "                  v[3] = 1\n",
    "              else:\n",
    "                  v[3] = -1\n",
    "\n",
    "          if v[4] == 1: \n",
    "              test_dt = ReviewDataset(tokenizer,test_arr[i:i+1]) \n",
    "              test_dl = torch.utils.data.DataLoader(test_dt,batch_size = 8,shuffle = False)\n",
    "              \n",
    "              pred_list = []\n",
    "    \n",
    "              model.load_state_dict(state_dict_status)  \n",
    "              pred_status = test_loop_emotion(test_dl, model, device) \n",
    "              pred_list.append(pred_status)\n",
    "                  \n",
    "              pred_status = np.mean(pred_list, axis=0)\n",
    "              pred_status = (pred_status > 0.5).astype(int)\n",
    "                        \n",
    "              if pred_status[0] == 1:\n",
    "                  v[4] = 1\n",
    "              else:\n",
    "                  v[4] = -1\n",
    "\n",
    "          if v[5] == 1: \n",
    "              test_dt = ReviewDataset(tokenizer,test_arr[i:i+1]) \n",
    "              test_dl = torch.utils.data.DataLoader(test_dt,batch_size = 8,shuffle = False)\n",
    "              \n",
    "              pred_list = []\n",
    "    \n",
    "              model.load_state_dict(state_dict_price)  \n",
    "              pred_price = test_loop_emotion(test_dl, model, device) \n",
    "              pred_list.append(pred_price)\n",
    "                  \n",
    "              pred_price = np.mean(pred_list, axis=0)\n",
    "              pred_price = (pred_price > 0.5).astype(int)\n",
    "                        \n",
    "              if pred_price[0] == 1:\n",
    "                  v[5] = 1\n",
    "              else:\n",
    "                  v[5] = -1\n",
    "\n",
    "          if v[6] == 1: \n",
    "              test_dt = ReviewDataset(tokenizer,test_arr[i:i+1]) \n",
    "              test_dl = torch.utils.data.DataLoader(test_dt,batch_size = 8,shuffle = False)\n",
    "              \n",
    "              pred_list = []\n",
    "    \n",
    "              model.load_state_dict(state_dict_thickness)  \n",
    "              pred_thickness = test_loop_emotion(test_dl, model, device) \n",
    "              pred_list.append(pred_thickness)\n",
    "                  \n",
    "              pred_thickness = np.mean(pred_list, axis=0)\n",
    "              pred_thickness = (pred_thickness > 0.5).astype(int)\n",
    "                        \n",
    "              if pred_thickness[0] == 1:\n",
    "                  v[6] = 1\n",
    "              else:\n",
    "                  v[6] = -1\n",
    "                  \n",
    "    pred = pd.DataFrame(pred,columns = ['색감','핏','재질','퀄리티','제품상태','가격','두께'])\n",
    "    review = pd.DataFrame(review).reset_index(drop = True)\n",
    "    pred = pd.concat([review,pred],axis = 1)\n",
    "    return pred"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "id": "41f3a424-d2d5-49ce-9a9e-429413753ea9",
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "eefc2ef662db497cab5246beed811068",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "  0%|          | 0/5545 [00:00<?, ?it/s]"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "/home/lab01/.local/lib/python3.10/site-packages/torch/_utils.py:776: UserWarning: TypedStorage is deprecated. It will be removed in the future and UntypedStorage will be the only storage class. This should only matter to you if you are using storages directly.  To access UntypedStorage directly, use tensor.untyped_storage() instead of tensor.storage()\n",
      "  return self.fget.__get__(instance, owner)()\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "05c05dac9aad44438af68d81464f3bec",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "  0%|          | 0/44356 [00:00<?, ?it/s]"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>리뷰</th>\n",
       "      <th>색감</th>\n",
       "      <th>핏</th>\n",
       "      <th>재질</th>\n",
       "      <th>퀄리티</th>\n",
       "      <th>제품상태</th>\n",
       "      <th>가격</th>\n",
       "      <th>두께</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>스트라이프 나시는 처음 사봤는데 살짝 포인트로 입기 너무 좋고 슬앤 특유의 모던한 ...</td>\n",
       "      <td>0</td>\n",
       "      <td>-1</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>처음 입어보는 민소매탑이라서 너무 튀지 않고 어디든 어울리는 무난템 골랐어용 줄무늬...</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>-1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>이거 두께감이 꽤 있어요 그만큼 탄탄해서 여름엔 좀 덥지만 맘에 듭니다!! 부유방 ...</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>나시와 셋뚜세뚜로 구입했어요 셔츠는 옷걸이에 걸어서 겉에 비닐 씌워서 보내주셨는데 ...</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>너무 맘에들어요! 길이가 좀 짧긴 한데 고개 숙여도 넥 부분 안쳐지고 딱 붙어있어서...</td>\n",
       "      <td>0</td>\n",
       "      <td>-1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>...</th>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>44351</th>\n",
       "      <td>키 168에 60인데 커요 박스형 찾으시면 괜찮을듯\\n저는 살짝 루즈핏에 여리여리 ...</td>\n",
       "      <td>0</td>\n",
       "      <td>-1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>44352</th>\n",
       "      <td>사이즈가 확실히 커서 좋아요\\n얇아서 초여름까지입고 실내활동만할때는 한여름에 가디건...</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>44353</th>\n",
       "      <td>색상 변경 문의드렸는데 친절하게 응대해주셔서 바꾼 색상으로 잘 받을 수 있었어요!!...</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>44354</th>\n",
       "      <td>퀄리티는 괜찮은데 모델 착샷보다 좀 많이 오버핏이고 색깔이 화면이랑은 좀 달라용 ㅠ</td>\n",
       "      <td>-1</td>\n",
       "      <td>-1</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>44355</th>\n",
       "      <td>별로 안비친다는 후기 많던데 엄청 비쳐서 살색까지 비쳐요(사진은 덜 비치게 나옴) ...</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>-1</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>44356 rows × 8 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "                                                      리뷰  색감  핏  재질  퀄리티  \\\n",
       "0      스트라이프 나시는 처음 사봤는데 살짝 포인트로 입기 너무 좋고 슬앤 특유의 모던한 ...   0 -1   1    0   \n",
       "1      처음 입어보는 민소매탑이라서 너무 튀지 않고 어디든 어울리는 무난템 골랐어용 줄무늬...   0  0   0    0   \n",
       "2      이거 두께감이 꽤 있어요 그만큼 탄탄해서 여름엔 좀 덥지만 맘에 듭니다!! 부유방 ...   0  1   0    1   \n",
       "3      나시와 셋뚜세뚜로 구입했어요 셔츠는 옷걸이에 걸어서 겉에 비닐 씌워서 보내주셨는데 ...   1  1   0    1   \n",
       "4      너무 맘에들어요! 길이가 좀 짧긴 한데 고개 숙여도 넥 부분 안쳐지고 딱 붙어있어서...   0 -1   0    0   \n",
       "...                                                  ...  .. ..  ..  ...   \n",
       "44351  키 168에 60인데 커요 박스형 찾으시면 괜찮을듯\\n저는 살짝 루즈핏에 여리여리 ...   0 -1   0    0   \n",
       "44352  사이즈가 확실히 커서 좋아요\\n얇아서 초여름까지입고 실내활동만할때는 한여름에 가디건...   0  1   0    0   \n",
       "44353  색상 변경 문의드렸는데 친절하게 응대해주셔서 바꾼 색상으로 잘 받을 수 있었어요!!...   1  0   0    0   \n",
       "44354     퀄리티는 괜찮은데 모델 착샷보다 좀 많이 오버핏이고 색깔이 화면이랑은 좀 달라용 ㅠ  -1 -1   0    1   \n",
       "44355  별로 안비친다는 후기 많던데 엄청 비쳐서 살색까지 비쳐요(사진은 덜 비치게 나옴) ...   0  0   0    0   \n",
       "\n",
       "       제품상태  가격  두께  \n",
       "0         0   0   1  \n",
       "1         0   1  -1  \n",
       "2         0   0   1  \n",
       "3         0   0   0  \n",
       "4         0   0   0  \n",
       "...     ...  ..  ..  \n",
       "44351     0   0   0  \n",
       "44352     0   0   0  \n",
       "44353     0   0   0  \n",
       "44354     0   0   0  \n",
       "44355     0   0  -1  \n",
       "\n",
       "[44356 rows x 8 columns]"
      ]
     },
     "execution_count": 16,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "pred = Review_classification(test_ft['리뷰'])\n",
    "pred"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "id": "76e13807-cbfd-4f6a-943a-0c8eb75acc7b",
   "metadata": {},
   "outputs": [],
   "source": [
    "test_ft.drop(columns = ['Unnamed: 0'],inplace = True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "id": "7fece078-ec46-48bb-b827-333975fde107",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(44356, 14)"
      ]
     },
     "execution_count": 22,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "review_44356 = pd.concat([test_ft,pred],axis = 1).copy()\n",
    "review_44356.shape"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "id": "2b7a9444-07fc-4baa-9f1a-27bdf474d1bf",
   "metadata": {},
   "outputs": [],
   "source": [
    "pred = pred.loc[:,['색감','핏','재질','퀄리티','제품상태','가격','두께']].copy()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "id": "07c2c95d-14f4-486c-9057-2052259eb6a4",
   "metadata": {},
   "outputs": [],
   "source": [
    "Demo_clothes = pd.concat([buying_concat,pred],axis = 1).copy()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "id": "71315aab-d639-4068-8a97-54f34390a339",
   "metadata": {},
   "outputs": [],
   "source": [
    "review_44356.to_excel('review_44356.xlsx', index=False)"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.10.13"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
