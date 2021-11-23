import streamlit as st
import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
import plotly.graph_objects as go
from plotly.graph_objects import Scatter
from plotly.offline import iplot, init_notebook_mode

import plotly.express as px
import plotly
import ipywidgets as ipw
import plotly.express as px
import ipywidgets
from ipywidgets import widgets

header = st.container()
dataset = st.container()
features = st.container()
model_training = st.container()

st.markdown(
    """
    <style>
    .main {
    background-color: #ECECF3;
    }
    </style>
    """,
    unsafe_allow_html= True
)

with header:
    st.title('ẢNH HƯỞNG CỦA ĐẠI DỊCH COVID – 19 ĐẾN MỘT SỐ NGÂN HÀNG TIÊU BIỂU CỦA VIỆT NAM GIAI ĐOẠN 2019 – 2021')
    st.subheader('Nhóm thực hiện: ')
    svC= ['Huỳnh Thanh Hải', 'Ngô Quý Trọng Trí', 'Hoàng Minh Quân']
    svT= ['Vũ Thị Hạnh Dung', 'Phan Thị Thùy Duyên', 'Nguyễn Tấn Sang']
    sv413= {'K20413C': svC, 'K20413T': svT}
    danhsach= pd.DataFrame(sv413)
    st.write(danhsach)

with dataset:
    st.header('Phân tích dữ liệu báo cáo tài chính ')
    st.subheader('Dữ liệu các số liệu phân tích: ')

    ACB = pd.read_excel("DATA FINAL.xlsx", sheet_name= "ACB")
    SCB = pd.read_excel("DATA FINAL.xlsx", sheet_name= "SCB")
    BID = pd.read_excel("DATA FINAL.xlsx", sheet_name= "BIDV")
    TPB = pd.read_excel("DATA FINAL.xlsx", sheet_name= "TPB")
    VCB = pd.read_excel("DATA FINAL.xlsx", sheet_name= "VCB")
    VTB = pd.read_excel("DATA FINAL.xlsx", sheet_name= "VTB")

    Quarter= ['Q1/2019', 'Q2/2019', 'Q3/2019', 'Q4/2019', 'Q1/2020', 'Q2/2020', 'Q3/2020', 'Q4/2020', 'Q1/2021', 'Q2/2021']

    #Earnings Before Taxes
    acb_ebt= ACB.iloc[10, 2:]
    scb_ebt= SCB.iloc[10, 2:]
    bid_ebt= BID.iloc[10, 2:]
    tpb_ebt= TPB.iloc[10, 2:]
    vcb_ebt= VCB.iloc[10, 2:]
    vtb_ebt= VTB.iloc[10, 2:]

    #Net Profit After Taxes
    acb_npat= ACB.iloc[11, 2:]
    scb_npat= SCB.iloc[11, 2:]
    bid_npat= BID.iloc[11, 2:]
    tpb_npat= TPB.iloc[11, 2:]
    vcb_npat= VCB.iloc[11, 2:]
    vtb_npat= VTB.iloc[11, 2:]

    #Net Profit
    acb_npr= ACB.iloc[12, 2:]
    scb_npr= SCB.iloc[12, 2:]
    bid_npr= BID.iloc[12, 2:]
    tpb_npr= TPB.iloc[12, 2:]
    vcb_npr= VCB.iloc[12, 2:]
    vtb_npr= VTB.iloc[12, 2:]

    #liquidity ratio
    a=ACB.iloc[2, 2:]
    v=VCB.iloc[2, 2:]
    s=SCB.iloc[2, 2:]
    vt=VTB.iloc[2, 2:]
    t=TPB.iloc[2, 2:]
    b=BID.iloc[2, 2:]

    #E/a
    a2=ACB.iloc[5, 2:]
    v2=VCB.iloc[5, 2:]
    s2=SCB.iloc[5, 2:]
    v2t=VTB.iloc[5, 2:]
    t2=TPB.iloc[5, 2:]
    b2=BID.iloc[5, 2:]

    #Non Performing Loan
    acb_npl= ACB.iloc[9, 2:]
    scb_npl= SCB.iloc[9, 2:]
    bid_npl= BID.iloc[9, 2:]
    tpb_npl= TPB.iloc[9, 2:]
    vcb_npl= VCB.iloc[9, 2:]
    vtb_npl= VTB.iloc[9, 2:]

    #Loans to customers
    a3=ACB.iloc[18, 2:]
    v3=VCB.iloc[18, 2:]
    s3=SCB.iloc[18, 2:]
    vt3=VTB.iloc[18, 2:]
    t3=TPB.iloc[18, 2:]
    b3=BID.iloc[18, 2:]

    #Credit growth
    acb_cg= ACB.iloc[14, 2:]
    scb_cg= SCB.iloc[14, 2:]
    bid_cg= BID.iloc[14, 2:]
    tpb_cg= TPB.iloc[14, 2:]
    vcb_cg= VCB.iloc[14, 2:]
    vtb_cg= VTB.iloc[14, 2:]
    
    #ROA
    acb_roa= ACB.iloc[16, 2:]
    scb_roa= SCB.iloc[16, 2:]
    bid_roa= BID.iloc[16, 2:]
    tpb_roa= TPB.iloc[16, 2:]
    vcb_roa= VCB.iloc[16, 2:]
    vtb_roa= VTB.iloc[16, 2:]

    #ROE
    acb_roe= ACB.iloc[17, 2:]
    scb_roe= SCB.iloc[17, 2:]
    bid_roe= BID.iloc[17, 2:]
    tpb_roe= TPB.iloc[17, 2:]
    vcb_roe= VCB.iloc[17, 2:]
    vtb_roe= VTB.iloc[17, 2:]

    #Due To Customers
    acb_dtc= ACB.iloc[19, 2:]
    scb_dtc= SCB.iloc[19, 2:]
    bid_dtc= BID.iloc[19, 2:]
    tpb_dtc= TPB.iloc[19, 2:]
    vcb_dtc= VCB.iloc[19, 2:]
    vtb_dtc= VTB.iloc[19, 2:]
    
with features:
    st.header('Lý do chọn đề tài: ')
    st.markdown('* Từ cuối năm 2019 đến nay, kinh tế thế giới, bao gồm Việt Nam, chịu ảnh hưởng nghiêm trọng bởi đại dịch COVID-19. Việc thực hiện giãn cách xã hội nhằm phục vụ công tác phòng, chống dịch bệnh COVID-19 đã phần nào ảnh hưởng đến quá trình sản xuất kinh doanh của các doanh nghiệp (DN) và làm giảm hiệu quả hoạt động kinh doanh của các ngân hàng thương mại. Đã có một vài nghiên cứu gần đây đánh giá rằng đại dịch COVID - 19 để lại cho toàn bộ hệ thống ngân hàng trên thế giới nhiều thiệt hại to lớn mà phải mất một khoảng thời gian dài mới có thể khôi phục. Riêng ở Việt Nam thì ngành ngân hàng cũng không ngoại lệ, nhận thấy được điều đó nên nhóm chúng tôi đã bắt đầu thực hiện một đề tài nhỏ nhằm xem xét và đánh giá mức độ ảnh hưởng của COVID -19 đến một vài ngân hàng tiêu biểu của Việt Nam như: BIDV, Vietcombank, Viettinbank, ACB, TP Bank, Saccombank… thông qua các hệ số về tỷ lệ thanh khoản, tỷ suất tự tài trợ (huy động vốn), tổng thu nhập...trong giai đoạn 2019-2021. Hy vọng những đóng góp và nghiên cứu mà nhóm chúng tôi đem lại sẽ có ích cho mọi người trong việc xem xét và đánh giá những vấn đề có liên quan đến tài chính.')
    st.header('Phạm vi nghiên cứu')
    st.subheader('Đối tượng nghiên cứu:')
    st.markdown('* Ảnh hưởng của đại dịch COVID -19 đến một số ngân hàng tiêu biểu của Việt Nam.')
    st.subheader('Phạm vi nghiên cứu:')
    st.markdown('* **Không gian nghiên cứu:** Đề tài tập trung nghiên cứu, đánh giá, nhận xét khả năng hoạt động của một vài ngân hàng trong lãnh thổ Việt Nam.')
    st.markdown('* **Thời gian nghiên cứu:** Trong bối cảnh dịch COVID giai đoạn từ 2019-2021.')


with model_training:
    st.header('Nội dung phân tích')
    st.subheader('Phân tích tỷ lệ thanh khoản:')
    st.markdown('- Về lý thuyết, tính thanh khoản của ngân hàng thương mại (NHTM) được xem như khả năng đáp ứng những nhu cầu tức thời về tiền của NHTM như rút tiền gửi và giải ngân các khoản tín dụng đã cam kết, chi trả chi phí hoạt động hay những nhu cầu cần phải thanh toán bằng tiền khác.')
   
    lr = go.Figure()
    lr.add_trace(go.Scatter(x=Quarter, y=a,
                        mode='lines+markers',
                        name='ACB'))
    lr.add_trace(go.Scatter(x=Quarter, y=b,
                        mode='lines+markers',
                        name='BIDV'))
    lr.add_trace(go.Scatter(x=Quarter, y=v,
                        mode='lines+markers',
                        name='VCB'))
    lr.add_trace(go.Scatter(x=Quarter, y=vt,
                        mode='lines+markers',
                        name='VTB'))
    lr.add_trace(go.Scatter(x=Quarter, y=s,
                        mode='lines+markers',
                        name='SCB'))
    lr.add_trace(go.Scatter(x=Quarter, y=t,
                        mode='lines+markers',
                        name='TPB'))
    lr.update_layout(title='Tỷ lệ thanh khoản của các ngân hàng qua các quý từ 2019-2021',yaxis_title='Tỷ lệ thanh khoản',
                    xaxis_title='Qúy 2019 - Qúy2021',barmode='group')
    lr.update_layout(
    autosize=False,
    width=900,
    height=400)
    st.plotly_chart(lr)
    st.subheader('Đánh giá:')
    st.markdown('* ')

    st.subheader('Phân tích tỷ lệ nợ xấu')
    st.markdown('- ')

    chart1 = go.Line(x= Quarter, y= acb_npl, opacity=0.75, name='ACB')
    chart2 = go.Line(x= Quarter, y= scb_npl, opacity=0.75, name='SCB')
    chart3 = go.Line(x= Quarter, y= bid_npl, opacity=0.75, name='BIDV')
    chart4 = go.Line(x= Quarter, y= tpb_npl, opacity=0.75, name='TPB')
    chart5 = go.Line(x= Quarter, y= vcb_npl, opacity=0.75, name='VCB')
    chart6 = go.Line(x= Quarter, y= vtb_npl, opacity=0.75, name='VTB')
    c1 = go.FigureWidget(data=(chart1, chart2, chart3, chart4, chart5, chart6),
                        layout=go.Layout(
                            title=dict(
                                text='Các khoản nợ ACB',
                            ),
                            barmode='group', yaxis_title='Ngàn tỷ', xaxis_title='Quý'
                        ))
    c1.update_layout(
    autosize=False,
    width=900,
    height=400)
    st.plotly_chart(c1)
    st.subheader('Đánh giá:')
    st.markdown('* ')

    st.subheader('Phân tích tỷ suất tự tài trợ')
    st.markdown('- ')

    Ea = go.Figure(data=[
        go.Bar(name='ACB', x= Quarter, y= a2),
        go.Bar(name='SCB', x= Quarter, y= s2),
        go.Bar(name='BID', x= Quarter, y= b2),
        go.Bar(name='TPB', x= Quarter, y= t2),
        go.Bar(name='VCB', x= Quarter, y= v2),
        go.Bar(name='VTB', x= Quarter, y= v2t),
    ])

    Ea.update_layout(title='Tỷ suất tự tài trợ của các ngân hàng qua các quý từ năm 2019-2021',
                    yaxis_title='Tỷ suất tự tài trợ',
                    xaxis_title='Qúy 2019 - Qúy2021',barmode='stack')
    Ea.update_layout(
    autosize=False,
    width=900,
    height=400)
    st.plotly_chart(Ea)
    st.subheader('Đánh giá:')
    st.markdown('* ')

    st.subheader('Phân tích lợi nhuận của ngân hàng')
    st.markdown('- ')
    trace13= go.Bar(name='ACB', x= Quarter, y= acb_ebt)
    trace14= go.Bar(name='SCB', x= Quarter, y= scb_ebt)
    trace15= go.Bar(name='BID', x= Quarter, y= bid_ebt)
    trace16= go.Bar(name='TPB', x= Quarter, y= tpb_ebt)
    trace17= go.Bar(name='VCB', x= Quarter, y= vcb_ebt)
    trace18= go.Bar(name='VTB', x= Quarter, y= vtb_ebt)
    g7 = go.FigureWidget(data=(trace13, trace14, trace15, trace16, trace17, trace18),
                        layout=go.Layout(
                            title=dict(
                                text='Lợi nhuận trước thuế của các ngân hàng'
                            ),
                            barmode='group', yaxis_title='Ngàn tỷ', xaxis_title='Quý'
                        ))
    g7.update_layout(
    autosize=False,
    width=900,
    height=400)
    st.plotly_chart(g7)
    trace19= go.Bar(name='ACB', x= Quarter, y= acb_npat)
    trace20= go.Bar(name='SCB', x= Quarter, y= scb_npat)
    trace21= go.Bar(name='BID', x= Quarter, y= bid_npat)
    trace22= go.Bar(name='TPB', x= Quarter, y= tpb_npat)
    trace23= go.Bar(name='VCB', x= Quarter, y= vcb_npat)
    trace24= go.Bar(name='VTB', x= Quarter, y= vtb_npat)
    g8 = go.FigureWidget(data=(trace19, trace20, trace21, trace22, trace23, trace24),
                        layout=go.Layout(
                            title=dict(
                                text='Lợi nhuận sau thuế của các ngân hàng'
                            ),
                            barmode='group', yaxis_title='Ngàn tỷ', xaxis_title='Quý'
                        ))
    g8.update_layout(
    autosize=False,
    width=900,
    height=400)
    st.plotly_chart(g8)
    npr = go.Figure(data=[
        go.Bar(name='ACB', y= acb_npr, x= Quarter),
        go.Bar(name='SCB', y= scb_npr, x= Quarter),
        go.Bar(name='BID', y= bid_npr, x= Quarter),
        go.Bar(name='TPB', y= tpb_npr, x= Quarter),
        go.Bar(name='VCB', y= vcb_npr, x= Quarter),
        go.Bar(name='VTB', y= vtb_npr, x= Quarter)
    ])
    npr.update_layout(title='Lợi nhuận ròng các ngân hàng qua các Quý',yaxis_title='Ngàn tỷ',
                    xaxis_title='Quý',barmode= 'stack')
    npr.update_layout(
        autosize=False,
        width=900,
        height=400)
    st.plotly_chart(npr)

    st.subheader('Đánh giá:')
    st.markdown('* ')

    st.subheader('Phân tích tăng trưởng tín dụng')
    st.markdown('- Về lý thuyết, tín dụng là mối quan hệ giữa người vay và người cho vay. Trong đó, người cho vay có nhiệm vụ chuyển giao quyền sử dụng tiền hoặc hàng hóa cho vay cho người đi  vay trong thời gian nhất định nào đó. Người đi vay có nghĩa vụ phải trả đủ số tiền hoặc hàng hóa đã đi vay khi đến hạn, có thể kèm hoặc không kèm theo lãi. Tín dụng ngân hàng là mối quan hệ tín dụng giữa ngân hàng (NH), các tổ chức tín dụng (TCTD) với các doanh nghiệp hay các cá nhân (bên đi vay). Trong đó, NH hay TCTD sẽ chuyển giao tài sản cho bên đi vay sử dụng trong một thời gian nhất định, khi đến hạn, bên đi vay phải hoàn trả cả gốc lẫn lãi cho TCTD.')
    st.markdown('- Tăng trưởng tín dụng là tổng tín dụng của toàn hệ thống ngân hàng trong năm nay sẽ lớn hơn năm trước. Ví dụ: Tăng trưởng tín dụng tăng 20% có nghĩa rằng tổng tín dụng của toàn hệ thống ngân hàng năm nay sẽ cao hơn so với năm trước là 20%.')

    cg = go.Figure(data=[
        go.Line(name='ACB', x= Quarter, y= acb_cg),
        go.Line(name='SCB', x= Quarter, y= scb_cg),
        go.Line(name='BID', x= Quarter, y= bid_cg),
        go.Line(name='TPB', x= Quarter, y= tpb_cg),
        go.Line(name='VCB', x= Quarter, y= vcb_cg),
        go.Line(name='VTB', x= Quarter, y= vtb_cg),
    ])
    cg.update_layout(title='Tăng trưởng tính dụng các ngân hàng',yaxis_title='Ngàn tỷ',
                    xaxis_title='Quý')
    cg.update_layout(
        autosize=False,
        width=900,
        height=400)
    st.plotly_chart(cg)

    st.subheader('Đánh giá:')
    st.markdown('* ')

    st.subheader('Phân tích tổng thu nhập của ngân hàng')
    st.markdown('- Về lý thuyết, Thu nhập ròng là khoản thu nhập trước thuế trừ đi khoản thuế thu nhập phải nộp cho ngân sách nhà nước, ngân sách địa phương của năm đó. (Thu nhập trước thuế là sự chênh lệch giữa tổng thu nhập hoạt động và tổng chi phí).')

    ltc = go.Figure(data=[
        go.Bar(name='ACB', x= Quarter, y= a3),
        go.Bar(name='SCB', x= Quarter, y= s3),
        go.Bar(name='BID', x= Quarter, y= b3),
        go.Bar(name='TPB', x= Quarter, y= t3),
        go.Bar(name='VCB', x= Quarter, y= v3),
        go.Bar(name='VTB', x= Quarter, y= vt3),
    ])

    ltc.update_layout(title='Tổng thu nhập của các ngân hàng qua các quý từ 2019-2021',yaxis_title='Thu nhập',
                    xaxis_title='Qúy 1 2019 - Qúy 2 2021',barmode='group')

    ltc.update_layout(
    autosize=False,
    width=900,
    height=400)
    st.plotly_chart(ltc)
    st.subheader('Đánh giá:')
    st.markdown('* ')

    st.subheader('Phân tích ROA - ROE')
    st.markdown('- ')
    st.markdown('- ')

    roa = go.Figure()
    roa.add_trace(go.Scatter(x=Quarter, y=acb_roa,
                        mode='lines+markers',
                        name='ACB'))
    roa.add_trace(go.Scatter(x=Quarter, y=bid_roa,
                        mode='lines+markers',
                        name='BIDV'))
    roa.add_trace(go.Scatter(x=Quarter, y=vcb_roa,
                        mode='lines+markers',
                        name='VCB'))
    roa.add_trace(go.Scatter(x=Quarter, y=vtb_roa,
                        mode='lines+markers',
                        name='VTB'))
    roa.add_trace(go.Scatter(x=Quarter, y=scb_roa,
                        mode='lines+markers',
                        name='SCB'))
    roa.add_trace(go.Scatter(x=Quarter, y=tpb_roa,
                        mode='lines+markers',
                        name='TPB'))
    roa.update_layout(yaxis_title='Phần trăm',
                    xaxis_title='Quý 2019 - Quý 2021',
                    title = dict(text = "ROA"),
                    font=dict(family="Arial, monospace", size=15, color="Black"),
                    barmode='group')
    roa.update_layout(
    autosize=False,
    width=900,
    height=400)
    st.plotly_chart(roa)
    st.subheader('Đánh giá:')
    st.markdown('* ')

    roe = go.Figure()
    roe.add_trace(go.Scatter(x=Quarter, y=acb_roe,
                        mode='lines+markers',
                        name='ACB'))
    roe.add_trace(go.Scatter(x=Quarter, y=bid_roe,
                        mode='lines+markers',
                        name='BIDV'))
    roe.add_trace(go.Scatter(x=Quarter, y=vcb_roe,
                        mode='lines+markers',
                        name='VCB'))
    roe.add_trace(go.Scatter(x=Quarter, y=vtb_roe,
                        mode='lines+markers',
                        name='VTB'))
    roe.add_trace(go.Scatter(x=Quarter, y=scb_roe,
                        mode='lines+markers',
                        name='SCB'))
    roe.add_trace(go.Scatter(x=Quarter, y=tpb_roe,
                        mode='lines+markers',
                        name='TPB'))
    roe.update_layout(yaxis_title='Phần trăm',
                    xaxis_title='Quý 2019 - Quý 2021',
                    title = dict(text = "ROE"),
                    font=dict(family="Arial, monospace", size=15, color="Black"),
                    barmode='group')
    roe.update_layout(
    autosize=False,
    width=900,
    height=400)
    st.plotly_chart(roe)
    st.subheader('Đánh giá:')
    st.markdown('* ')

    st.subheader('Tiền gửi trong các ngân hàng')
    st.markdown('- ')

    dtc = go.Figure(data=[
        go.Line(name='ACB', y= acb_dtc, x= Quarter),
        go.Line(name='SCB', y= scb_dtc, x= Quarter),
        go.Line(name='BID', y= bid_dtc, x= Quarter),
        go.Line(name='TPB', y= tpb_dtc, x= Quarter),
        go.Line(name='VCB', y= vcb_dtc, x= Quarter),
        go.Line(name='VTB', y= vtb_dtc, x= Quarter),
    ])

    dtc.update_layout(title='Tiền gửi ngân hàng',yaxis_title='Ngàn tỷ',
                    xaxis_title='Quý')

    dtc.update_layout(
    autosize=False,
    width=900,
    height=400)
    st.plotly_chart(dtc)
    st.subheader('Đánh giá:')
    st.markdown('* ')
