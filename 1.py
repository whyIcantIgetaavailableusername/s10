import streamlit as st
price_list = []
st.title('CoTAI Boba Tea')
col1,col2 = st.columns(2)
with col1:
  st.image('https://imgur.com/lEpdPsT.png')
with col2:
  size = st.radio('Kích cỡ', ('Nhỏ(30k)','Vừa(40k)','Lớn(50k)'), horizontal=True)
  st.write('Thêm')
  col3,col4 = st.columns(2)
  with col3:
    them_list = []
    s = st.checkbox('Sữa(5k)')
    cp = st.checkbox('Cà phê(8k)')
  with col4:
    k = st.checkbox('Kem(10k)')
    tr = st.checkbox('Trứng(15k)')
col5,col6 = st.columns(2)
with col5:
  Topping = st.multiselect('Toppings', ('Trân châu trắng (5K)','Trân châu đen (5K)','Thạch rau câu (6K)','Vải (7K)','Nhãn (8K)','Đào (10K)'))
with col6:
  amount = st.number_input('Số lượng',0)
Ghichu = st.text_area('Ghi chú')
size_list = ['Nhỏ(30k)','Vừa(40k)','Lớn(50k)']
price_size_list = [30,40,50]
Topping_list = ['Trân châu trắng (5K)','Trân châu đen (5K)','Thạch rau câu (6K)','Vải (7K)','Nhãn (8K)','Đào (10K)']
price_Topping_list = [5,5,6,7,8,10]
def calculate(original,stri,price):
  for i,j in zip(stri,price):
    for n in original:
      if i == n:
        price_list.append(j)
if st.button('Đặt hàng', use_container_width=True):
  if size == 'Nhỏ(30k)':
    des = 'nhỏ'
  elif size == 'Vừa(40k)':
    des = 'vừa'
  else:
    des = 'Lớn'
  if s:
    price_list.append(5)
    them_list.append('Sữa')
  if cp:
    price_list.append(8)
    them_list.append('Cà phê')
  if k:
    price_list.append(10)
    them_list.append('Kem')
  if tr:
    price_list.append(15)
    them_list.append('Trứng')
  size = [size]
  calculate(size,size_list,price_size_list)
  calculate(Topping,Topping_list,price_Topping_list)
  Topping_des = str(Topping[0]) 
  them_des = str(them_list[0])
  if len(Topping) > 1:
      for i in range(1,len(Topping)):
        Topping_des = Topping_des + ', ' + Topping[i]
  if len(them_list) > 1:
      for i in range(1,len(them_list)):
        them_des = them_des + ', ' + them_list[i]
  price = sum(price_list)*amount
  price = str(price) + 'K'
  st.text(f'''Cỡ, {des}
Thêm: {them_des}
Topping: {Topping_des}
{Ghichu}
Số lượng: {amount}
Thành tiền: {price}
''')









# for i,j in zip(size_list,price_list):





     

