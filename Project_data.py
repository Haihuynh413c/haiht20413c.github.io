import streamlit as st
import pandas as pd
import numpy as np

import plotly.graph_objects as go
from plotly.graph_objects import Scatter
from plotly.offline import iplot, init_notebook_mode

import plotly.express as px
import plotly
import plotly.express as px
from PIL import Image
from streamlit.proto.Markdown_pb2 import Markdown

header = st.container()
dataset = st.container()
features = st.container()
model_training = st.container()

st.markdown(
    """
    <style>
    .main {
    background-image: url("https://scontent.fsgn5-10.fna.fbcdn.net/v/t1.15752-9/p1080x2048/260880588_429083302137853_1486874591801723903_n.png?_nc_cat=110&ccb=1-5&_nc_sid=ae9488&_nc_ohc=bLyPN_HxqyYAX8NJO2k&tn=sZ3veoGUVIgZwJzX&_nc_ht=scontent.fsgn5-10.fna&oh=09ac50455be5c14adc8ef9135fc439ca&oe=61C67E3A");
    background-color: #FFF0F5;
    }
    </style>
    """,
    unsafe_allow_html= True
)

rad= st.sidebar.radio('Chọn mục:', ['Trang chủ','Giới thiệu','Tăng trưởng tín dụng', 'Tỷ lệ nợ xấu', 'Tiền gửi ngân hàng', 'Tỷ lệ thanh khoản', 'Tăng trưởng tín dụng', 'Lợi nhuận', 'ROA - ROE', 'Tỷ suất tự tài trợ', 'Thu nhập của ngân hàng', 'Thu nhập từ dịch vụ', 'Kết luận', 'Lời cảm ơn'])

with header:
    if rad == 'Giới thiệu':
        st.header('Nhóm thực hiện: ')
        st.image('https://scontent.fsgn5-5.fna.fbcdn.net/v/t1.15752-9/260367270_1328822517566296_2527763412141226313_n.png?_nc_cat=108&ccb=1-5&_nc_sid=ae9488&_nc_ohc=YBCPItxMrsoAX_8MjXe&tn=sZ3veoGUVIgZwJzX&_nc_ht=scontent.fsgn5-5.fna&oh=a15522f380a2dff5703a59cfea8bc5ef&oe=61C1D4DC')
        st.header('Phân tích dữ liệu báo cáo tài chính ')
        st.subheader('Nguồn dữ liệu: ')
        st.markdown('- Ngân hàng nhà nước VN')
        st.markdown('- Trung tâm nghiên cứu Kinh tế và Tài chính, trường Đại học Kinh tế - Luật ĐHQG-HCM')
        st.markdown('- Báo cáo tài chính của các ngân hàng qua các quý (Quý I 2019 - Quý II 2021)')
        st.header('Lý do chọn đề tài: ')
        st.markdown('* Từ cuối năm 2019 đến nay, kinh tế thế giới, bao gồm Việt Nam, chịu ảnh hưởng nghiêm trọng bởi đại dịch COVID-19. Việc thực hiện giãn cách xã hội nhằm phục vụ công tác phòng, chống dịch bệnh COVID-19 đã phần nào ảnh hưởng đến quá trình sản xuất kinh doanh của các doanh nghiệp (DN) và làm giảm hiệu quả hoạt động kinh doanh của các ngân hàng thương mại. Đã có một vài nghiên cứu gần đây đánh giá rằng đại dịch COVID - 19 để lại cho toàn bộ hệ thống ngân hàng trên thế giới nhiều thiệt hại to lớn mà phải mất một khoảng thời gian dài mới có thể khôi phục. Riêng ở Việt Nam thì ngành ngân hàng cũng không ngoại lệ, nhận thấy được điều đó nên nhóm chúng tôi đã bắt đầu thực hiện một đề tài nhỏ nhằm xem xét và đánh giá mức độ ảnh hưởng của COVID -19 đến một vài ngân hàng tiêu biểu của Việt Nam như: BIDV, Vietcombank, Viettinbank, ACB, TP Bank, Saccombank… thông qua các hệ số về tỷ lệ thanh khoản, tỷ suất tự tài trợ (huy động vốn), tổng thu nhập...trong giai đoạn 2019-2021. Hy vọng những đóng góp và nghiên cứu mà nhóm chúng tôi đem lại sẽ có ích cho mọi người trong việc xem xét và đánh giá những vấn đề có liên quan đến tài chính.')
        st.header('Phạm vi nghiên cứu')
        st.subheader('Đối tượng nghiên cứu:')
        st.markdown('* Ảnh hưởng của đại dịch COVID -19 đến một số ngân hàng tiêu biểu của Việt Nam.')
        st.subheader('Phạm vi nghiên cứu:')
        st.markdown('* **Không gian nghiên cứu:** Đề tài tập trung nghiên cứu, đánh giá, nhận xét khả năng hoạt động của một vài ngân hàng trong lãnh thổ Việt Nam.')
        st.markdown('* **Thời gian nghiên cứu:** Trong bối cảnh dịch COVID giai đoạn từ 2019-2021.')

with dataset:
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

    #Net Fee And Commission Income
    acb_nfci=ACB.iloc[20, 2:]
    vcb_nfci=VCB.iloc[20, 2:]
    scb_nfci=SCB.iloc[20, 2:]
    vtb_nfci=VTB.iloc[20, 2:]
    tpb_nfci=TPB.iloc[20, 2:]
    bid_nfci=BID.iloc[20, 2:]
    
with features:
    if rad == 'Trang chủ':
        st.balloons()
        st.header('ẢNH HƯỞNG CỦA ĐẠI DỊCH COVID – 19 ĐẾN MỘT SỐ NGÂN HÀNG TIÊU BIỂU CỦA VIỆT NAM GIAI ĐOẠN 2019 – 2021')
        st.image('https://scontent.fsgn5-6.fna.fbcdn.net/v/t1.15752-9/260511541_355997596285226_9004633310030532007_n.png?_nc_cat=106&ccb=1-5&_nc_sid=ae9488&_nc_ohc=4zg9pJU2reAAX-gTxSf&_nc_ht=scontent.fsgn5-6.fna&oh=ee2c285563aa82004e859035c195839b&oe=61C4574F')
        

with model_training:
    if rad == 'Tỷ lệ thanh khoản':
        st.subheader('Phân tích tỷ lệ thanh khoản:')
        with st.expander("Lý thuyết:"):
            st.write("- Về lý thuyết, tính thanh khoản của ngân hàng thương mại (NHTM) được xem như khả năng đáp ứng những nhu cầu tức thời về tiền của NHTM như rút tiền gửi và giải ngân các khoản tín dụng đã cam kết, chi trả chi phí hoạt động hay những nhu cầu cần phải thanh toán bằng tiền khác.")
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
        width=750,
        height=400)
        st.plotly_chart(lr)
        with st.expander("Đánh giá:"):
            st.write('''* Nhìn chung, năm 2019 là một năm có thanh khoản hệ thống dồi dào, cho phép lãi suất giữ ở
            mức tương đối thấp. Lãi xuất qua đêm liên ngân hàng có xu hướng giảm trong 10 tháng đầu năm
            2019 xuống mức 2%. Lãi suất này chỉ tạm thời tăng ở một số ngân hàng trong tháng 11, khi Kho
            bạc nhà nước thu lại các khoản gửi không kì hạn tại các ngân hàng thương mai (01/11/2019) theo
            Nghị định 58/ 2019. Lãi suất thấp cũng ảnh hưởng đến Trái phiếu chính phủ, cụ thể lãi suất trái
            phiếu trong 10 tháng đầu năm giảm xuống gần 3.65% vào cuối tháng 12. Đến năm 2020, khi mà
            tăng trưởng tín dụng đang được tăng cao thì kéo theo tỉ lệ thanh khoản cho cả ngân hàng tư nhân
            lẫn ngân hàng quốc doang cũng dồi dào hơn. Trong giai đoạn này tăng trưởng tín dụng có thể
            suy yếu do cả nước phải đối mặt với làn sóng COVID - 19 thứ hai trong khi các ngân hàng không
            hạ tiêu chí cấp tín dụng. Cho vay khách hàng doanh nghiệp và trái phiếu doanh nghiệp lớn chính
            là động lực để tăng trưởng tín dụng, đồng thời tạo ra thanh khoản dồi dào cho các ngân hàng
            thương mại. Tăng trưởng tín dụng vào cuối năm 2020 sẽ được duy trì mạnh mẽ, và tiếp tục tạo
            thanh khoản tốt cho các ngân hàng. Trong hai quý đầu năm 2021, tuy có ảnh hưởng khá nặng của
            đại dịch, nhưng tỷ lệ thanh khoản của các ngân hàng quốc doanh như Vietcombank, hay BIDV…
            vẫn giữ được mức thanh khoản ổn định, thậm chí có tháng tăng cao. Riêng các ngân hàng tư nhân
            có một vài ngân hàng có rục rịch giảm thanh khoản như TP Bank, Saccombank.. nhưng những
            con số đó giảm không đáng kể và vẫn giữ ở mức trung bình cao, khá là ổn định cho các ngân
            hàng nói chung. Mặc dù có dịch nhưng tỉ lệ giao dịch giữa các ngân hàng vẫn tăng cao, chỉ qua
            là thay đổi hinhd thức giao dịch thôi nên ảnh hưởng đến tính thanh khoản không nhiều.''')
    if rad == 'Tỷ lệ nợ xấu':
        st.subheader('Phân tích tỷ lệ nợ xấu')
        with st.expander("Lý thuyết:"):
            st.write('- Tỷ lệ nợ xấu phản ánh chất lượng và mức độ rủi ro của danh mục cho vay mà ngân hàng có, số lượng đồng nợ xấu trên tổng số 100 đồng cho vay.')
            st.write('- Khi ngân hàng gặp rắc rối hoặc có vấn đề trong việc quản lý chất lượng các khoản vay từ khách thì tỷ lệ nợ xấu có tình trạng tăng cao hơn trung bình trong ngành và có chiều hướng tăng lên.')
            st.write('- Khi tỷ lệ này thấp so với trung bình ngành và có chiều hướng giảm tức là ngân hàng đang quản lý tốt các khoản vay tín dụng. Hoặc cũng có trường hợp ngân hàng dùng chính sách xóa nợ, thay đổi các phân loại của khoản nợ.')
        chart1 = go.Line(x= Quarter, y= acb_npl, opacity=0.75, name='ACB')
        chart2 = go.Line(x= Quarter, y= scb_npl, opacity=0.75, name='SCB')
        chart3 = go.Line(x= Quarter, y= bid_npl, opacity=0.75, name='BIDV')
        chart4 = go.Line(x= Quarter, y= tpb_npl, opacity=0.75, name='TPB')
        chart5 = go.Line(x= Quarter, y= vcb_npl, opacity=0.75, name='VCB')
        chart6 = go.Line(x= Quarter, y= vtb_npl, opacity=0.75, name='VTB')
        c1 = go.FigureWidget(data=(chart1, chart2, chart3, chart4, chart5, chart6),
                            layout=go.Layout(
                                title=dict(
                                    text='Tỷ lệ nợ xấu của các ngân hàng',
                                ),
                                barmode='group', yaxis_title='Ngàn tỷ', xaxis_title='Quý'
                            ))
        c1.update_layout(
        autosize=False,
        width=750,
        height=400)
        st.plotly_chart(c1)
        with st.expander("Đánh giá:"):
            st.write("""* Tính đến tháng 6 năm 2020, tổng nợ tái cơ cấu theo toàn ngành ngân hàng theo thông tư 01 là
            177 nghìn tỷ đồng tương đường 2.1% tổng tín dụng. Đối với 6 ngân hàng năm trong phạm vi
            nghiên cứu của nhóm thì thì nợ vay tái cơ cấu tăng lên đến gần 100 nghìn tỷ đồng tương đương
            2.7% tổng dư nợ , trong đó BIDV và TP Bank chiếm hơn một nửa dư nợ. Nợ xấu tăng 18,%YTD,
            cho thấy tình trạng của nợ xấu đã bắt đầu tăng trong năm 2020. Tỷ lệ nợ xấu trung bình tăng của
            các ngân hàng hầu như đều tăng trong giai đoạn này, chỉ có một vài ngân hàng như Vietcombank
            hay Viettinbank là ngân hàng có tỷ lệ nợ xấu giảm phần lớn là do tích cực xóa nợ và tái cơ cấu
            nợ lớn. Theo đánh giá, trong giai đoạn cuối năm 2020, nợ tái cơ cấu và nợ xấu sẽ tăng nhanh hơn
            nữa. Dựa vào ước tính của Ngân hàng Nhà nước vào Quý 1/ 2020 thì tỷ lệ tín dụng giảm và nợ
            xấu tăng là do ảnh hưởng chủ yếu của đại dịch COVID -19. Khi đại dịch kéo dài thì số lượng
            khách hàng khó khăn về dòng tiền tiếp tục tăng lên dẫn đến các ngân hàng phải đưa các khoản
            nợ này vào nợ tái cơ cấu hoặc đành chấp nhận phân loại thành nợ xấu. Do đó mà thu nhập lãi
            mất đi liên quan đến tái cơ cấu và nợ xấu có thể ở mức đáng kể hơn.""")
            st.write("""* Đến đầu năm 2021 thì tác động của đại dịch COVID 19 dần dần được phản ánh rõ trong số dư
            nợ xấu của các ngân hàng. Mặc dù chi phí dự phòng trong quý 3 , quý 4 năm 2020 tăng 18%, so
            với trước phần lớn trong số đó dùng cho mục đích xóa nợ nhưng tỷ lệ nợ xấu của các ngân hàng
            vẫn tăng lên 1.77%, tỷ lệ dự phòng bao nợ xấu chỉ nhích nhẹ.""")
            st.write("""- Quý 1/2021, một vài ngân hàng có số dư nợ xấu tăng, trong đó một số ngân hàng tăng mạnh
            trên 30% như ACB, Vietcombank,… ACB là ngân hàng có nợ xấu tăng mạnh nhất trong quý đầu
            năm nay, tăng 61% lên 2.954 tỷ đồng.""")
            st.write("""- Mặc dù các ngân hàng đã công bố những kết quả khả quan về tăng trưởng lợi nhuận của năm
            2021 của ngành, tuy nhiên theo nhiều nguồn tin, các ngân hàng cũng rất “nặng gánh” với vấn đề
            nợ xấu. Việc kiểm soát nợ xấu thời gian tới sẽ khó khăn thách thức rất lớn đối với ngành ngân
            hàng và nhất là khối Ngân hàng TMCP Nhà nước trong năm 2021. Trước thực tế khối nợ xấu
            tiếp tục xu hướng “phình to” trong năm 2021, để kiểm soát rủi ro nợ xấu, bên cạnh việc tích cực
            xử lý nợ xấu, các ngân hàng cũng cần chủ động trích lập dự phòng rủi ro cho các khoản nợ xấu
            và tiềm ẩn nợ xấu.""")
    if rad == 'Tỷ suất tự tài trợ':
        st.subheader('Phân tích tỷ suất tự tài trợ')
        with st.expander("Lý thuyết:"):
            st.write('- Về lý thuyết, Hh số này phản ánh tỷ trọng nguồn vốn chủ sở hữu trên tổng tài sản của doanh nghiệp. Để xác định mức độ phù hợp về tỷ lệ vốn chủ sở hữu trong trong nguồn vốn của doanh nghiệp sẽ phụ thuộc rất lớn vào hoạt động và chính sách của từng doanh nghiệp cũng như từng ngành.')
            st.write('- Tỷ số này cao chứng tỏ khả năng tự chủ tài chính của doanh nghiệp, nhưng cũng cho thấy doanh nghiệp chưa tận dụng đòn bẩy tài chính nhiều.')
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
        width=750,
        height=400)
        st.plotly_chart(Ea)
        with st.expander("Đánh giá:"):
            st.write("""- Trong bối cảnh nguy cơ nợ xấu tiếp tục tăng mạnh, nhiều ngân hàng đã mạnh tay trích lập dự
            phòng rủi ro cho vay, tăng "sức đề kháng" trước bão COVID-19.""")
            st.write("""- Tổng chi phí dự phòng rủi ro tín dụng của ngân hàng niêm yết cũng đã ghi nhận mức tăng 20%
            YoY trong năm vừa qua do tác động của đại dịch Covid-19.Chúng tôi cho rằng việc tăng mạnh
            chi phí trích lập dự phòng của các NHTM trong năm vừa qua nhằm tạo ra bộ đệm vốn giúp cho
            các nhà băng có thể chống chọi lại tác động của đại dịch Trong năm 2021, chúng tôi cho rằng
            chi phí trích lập dự phòng có thể sẽ không tăng đột biến như năm 2020 khi nền kinh tế cho thấy
            sự hồi phục mạnh mẽ, qua đó giúp cho các khoản nợ không bị chuyển nhóm. Đồng thời thông tư
            03 vừa được ban hành cũng sẽ phần nào giúp cho áp lực trích lập của NHTM phần nào giảm bớt.
            Biểu đồ cho thấy tỷ suất này có xu hướng đi ngang và tăng nhẹ nhờ vào chất lượng tài sản được
            duy trì ổn định và các khoản vay tái cơ cấu hồi phục tốt sau đại dịch so với năm 2020 và đây là
            dấu hiệu hỗ trợ tích cực cho giai đoạn phục hồi kinh tế sau đại dịch.Theo dự báo, các NHTM có
            yếu tố nhà nước trong năm 2021 sẽ ghi nhận tốc độ tăng trưởng lợi nhuận vượt trội so với nhóm
            NHTM tư nhân nhờ tỷ lệ NIM tăng mạnh và chi phí trích lập dự phòng ổn định hơn trong năm
            2021.""")
    if rad== 'Lợi nhuận':
        st.subheader('Phân tích lợi nhuận của ngân hàng')
        with st.expander("Lý thuyết:"):
            st.subheader('Lợi nhuận trước thuế:')
            st.write('- Về lý thuyết, lợi nhuận trước thuế (EBT) là số lợi nhuận mà doanh nghiệp thu về sau khi đã trừ đi phần tiền bỏ ra để kinh doanh. Nhưng chưa kể đến thuế phải nộp nhà nước và tiền lãi. Lợi nhuận trước thuế bao gồm lợi nhuận thu về từ hoạt động sản xuất kinh doanh, lợi nhuận tài chính và lợi nhuận phát sinh. ')
        bang = st.selectbox('Chọn mục:', ('ACB', 'SCB', 'BIDV', 'TPB', 'VCB', 'VTB','Lợi nhuận trước thuế của các ngân hàng'))
        if bang == 'ACB':
            acb_bd= go.Figure(data=[
                go.Bar(x= Quarter, y= acb_ebt, opacity=0.75, name='Lợi nhuận trước thuế'),
                go.Bar(x= Quarter, y= acb_npat, opacity=0.75, name='Lợi nhuận sau thuế')
            ])
            acb_bd.update_layout(title='Lợi nhuận trước và sau thuế của ACB',
                        yaxis_title='Ngàn tỷ',
                        xaxis_title='Quý',barmode='group')
            acb_bd.update_layout(
            autosize=False,
            width=750,
            height=400)
            st.plotly_chart(acb_bd)
        elif bang == 'SCB':
            scb_bd= go.Figure(data=[
                go.Bar(x= Quarter, y= scb_ebt, opacity=0.75, name='Lợi nhuận trước thuế'),
                go.Bar(x= Quarter, y= scb_npat, opacity=0.75, name='Lợi nhuận sau thuế')
            ])
            scb_bd.update_layout(title='Lợi nhuận trước và sau thuế của SCB',
                        yaxis_title='Ngàn tỷ',
                        xaxis_title='Quý',barmode='group')
            scb_bd.update_layout(
            autosize=False,
            width=750,
            height=400)
            st.plotly_chart(scb_bd)
        elif bang == 'BIDV':
            bid_bd= go.Figure(data=[
                go.Bar(x= Quarter, y= bid_ebt, opacity=0.75, name='Lợi nhuận trước thuế'),
                go.Bar(x= Quarter, y= bid_npat, opacity=0.75, name='Lợi nhuận sau thuế')
            ])
            bid_bd.update_layout(title='Lợi nhuận trước và sau thuế của BIDV',
                        yaxis_title='Ngàn tỷ',
                        xaxis_title='Quý',barmode='group')
            bid_bd.update_layout(
            autosize=False,
            width=750,
            height=400)
            st.plotly_chart(bid_bd)
        elif bang == 'TPB':
            tpb_bd= go.Figure(data=[
                go.Bar(x= Quarter, y= tpb_ebt, opacity=0.75, name='Lợi nhuận trước thuế'),
                go.Bar(x= Quarter, y= tpb_npat, opacity=0.75, name='Lợi nhuận sau thuế')
            ])
            tpb_bd.update_layout(title='Lợi nhuận trước và sau thuế của TPB',
                        yaxis_title='Ngàn tỷ',
                        xaxis_title='Quý',barmode='group')
            tpb_bd.update_layout(
            autosize=False,
            width=750,
            height=400)
            st.plotly_chart(tpb_bd)
        elif bang == 'VCB':
            vcb_bd= go.Figure(data=[
                go.Bar(x= Quarter, y= vcb_ebt, opacity=0.75, name='Lợi nhuận trước thuế'),
                go.Bar(x= Quarter, y= vcb_npat, opacity=0.75, name='Lợi nhuận sau thuế')
            ])
            vcb_bd.update_layout(title='Lợi nhuận trước và sau thuế của VCB',
                        yaxis_title='Ngàn tỷ',
                        xaxis_title='Quý',barmode='group')
            vcb_bd.update_layout(
            autosize=False,
            width=750,
            height=400)
            st.plotly_chart(vcb_bd)
        elif bang == 'VTB':
            vtb_bd= go.Figure(data=[
                go.Bar(x= Quarter, y= acb_ebt, opacity=0.75, name='Lợi nhuận trước thuế'),
                go.Bar(x= Quarter, y= acb_npat, opacity=0.75, name='Lợi nhuận sau thuế')
            ])
            vtb_bd.update_layout(title='Lợi nhuận trước và sau thuế của VTB',
                        yaxis_title='Ngàn tỷ',
                        xaxis_title='Quý',barmode='group')
            vtb_bd.update_layout(
            autosize=False,
            width=750,
            height=400)
            st.plotly_chart(vtb_bd)
        elif bang == 'Lợi nhuận trước thuế của các ngân hàng':
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
            width=750,
            height=400)
            st.plotly_chart(g7)
        with st.expander("Đánh giá:"):
            st.write("""- Nhóm các ngân hàng đáp ứng chuẩn Basel II và đã hoàn tất quá trình xử lý nợ tồn đọng còn
            nhiều động lực tăng trưởng. Tăng trưởng tín dụng được ưu tiên ở mức cao hơn giúp lợi nhuận
            tiếp tục bứt tốc mạnh mẽ với NIM được mở rộng. Thu nhập ngoài lãi được tài trợ phần lớn bởi
            thu nhập dịch vụ và thu nhập khác từ nợ đã xoá.""")
            st.write('''- Nhóm ngân hàng còn lại tiếp tục quá trình tái cơ cấu. Nợ tồn đọng lớn sẽ hạn chế khả năng tăng
            trưởng tín dụng và làm giảm đáng kể lợi nhuận của một số ngân hàng. Tăng vốn là vấn đề cấp
            bách để nhóm này đáp ứng chuẩn an toàn hoạt động của hệ thống. Vốn điều lệ/vốn chủ sở hữu
            được tăng cường là bàn đạp vững chắc để các ngân hàng có nguồn lực để xử lý nợ tồn đọng cũng
            như đầu tư cho hoạt động kinh doanh để có thể bứt phá tăng trưởng trong dài hạn.Lợi nhuận
            trước thuế hợp nhất năm 2019 ở mức rất cao, tăng khoảng 30%, so với năm 2018 và vượt 5% kế
            hoạch được Đại hội cổ đông thông qua trong khi tỷ lệ nợ xấu ở mức rất thấp, dưới 1%.''')
            st.write('''- Kết quả kinh doanh đáng khích lệ trong Q3/2020 với tổng lợi nhuận trước thuế đạt 29,7 nghìn
            tỷ đồng (+6,6%. so với cùng kỳ). Thoạt nhìn, kết quả này có vẻ tương đối thấp so với mức tăng
            trưởng lợi nhuận trước thuế ấn tượng của Q2/2020 (+24,6%. so với cùng kỳ). Trên thực tế, mức
            sụt giảm -21% lợi nhuận trước thuế của VCB trong Q3 đã tác động tiêu cực đến kết quả chung
            của toàn ngành. Nếu loại trừ VCB, lợi nhuận trước thuế được cải thiện ở mức +14,7%, so với
            cùng kỳ trong Q3/2020 do tổng thu nhập hoạt động tăng trưởng mạnh (+14%. so với cùng kỳ) và
            sư gia tăng thấp hơn của chi phí dự phòng(+5,7%. so với cùng kỳ) và chi phí hoạt động (+10%
            so với cùng kỳ). Tuy nhiên, đáng chú ý là mức trích lập dự phòng khác biệt đáng kể giữa SOCB
            (ngân hàng thương mại nhà nước -NHTMNN) và JSCB (ngân hàng thương mại cổ phần -
            NHTMCP). Trong khi VCB và VTB có mức trích lập dự phòng tăng từ 35% đến 39%, thì JSCBs
            lại giảm -10,7%, so với cùng kỳ.''')
            st.write('''- Lũy kế 9T2020, lợi nhuận trước thuế của các ngân hàng mà chúng tôi nghiên cứu đạt 86,2 nghìn
            tỷ đồng (+11%. so với cùng kỳ). Mặc dù tốc độ tăng trưởng thấp hơn nhiều so với mức tăng lợi
            nhuận trước thuế là 26,9%, của cùng kỳ năm 2019, hoạt động của ngành vẫn vượt trội so với các
            ngành khác. NHTMCP là động lực chính của lợi nhuận trước thuế trong Q3/2020. Lợi nhuận
            trước thuế của các ngân hàng tư nhân tăng 18,6%, so với cùng kỳ, trong khi lợi nhuận trước thuế
            của các NHTMNN chỉ tăng +0,9%, so với cùng kỳ. Dẫn đầu Q4/2019 với Q1/2021 là ngân hàng
            VTB và VCB''')
            st.write("""- Triển vọng chung của ngành ngân hàng tốt hơn so với ước tính trước đây do ít bị ảnh hưởng từ
            đợt bùng phát thứ 2 của dịch Covid-19, chúng tôi điều chỉnh tăng ước tính lợi nhuận trước thuế
            cho các ngân hàng chúng tôi nghiên cứu lên +9,2% và +10,5%, cho năm 2020 và 2021, tương
            ứng đạt 110,7 nghìn tỷ đồng (+2,7%. so với cùng kỳ) và 129,3 nghìn tỷ đồng (+16,8%. so với
            cùng kỳ). Chúng tôi ước tính lợi nhuận trước thuế của các NHTMNN giảm -6,2% trong năm
            2020, và sau đó phục hồi +21,8% trong năm 2021. Trong khi đó, chúng tôi ước tính lợi nhuận
            trước thuế của các NHTMCP sẽ tăng trưởng + 9,3% trong năm 2020 và tăng +13,7% trong năm
            2021. Do đó, chúng tôi đánh giá KHẢ QUAN đối với ngành ngân hàng trong năm 2021. Các yếu
            tố hỗ trợ tích cực liên quan đến cổ tức bằng cổ phiếu cũng sẽ hỗ trợ tăng giá của cổ phiếu ngân
            hàng trong Q4/2020.""")
        st.subheader('Lợi nhuận sau thuế (lãi ròng)')
        with st.expander('Lý thuyết:'):
            st.subheader('Lợi nhuận sau thuế:')
            st.write('- Về lý thuyết, lợi nhuận sau thuế chính là khoản lợi nhuận cuối cùng của doanh nghiệp. Lợi nhuận sau thuế có được khi lấy doanh thu trừ đi tổng chi phí và thuế phải nộp nhà nước. Lợi nhuận sau thuế còn được gọi với tên khác là lợi nhuận ròng ( lãi ròng).')
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
            width=750,
            height=400)
        st.plotly_chart(npr)
        with st.expander("Đánh giá:"):
            st.write("""* Mặc dù thu nhập lãi thuần tăng trưởng tương đối ổn định trong quý đầu tiên của năm 2020, tuy
            vậy LNST của các ngân hàng chỉ tăng trưởng khoảng 3%. Tương tự như thu nhập lãi, các NHTM
            không có vốn nhà nước có mức tăng trưởng nhìn chung tốt hơn so với các NHTM quốc doanh.
            Các NHTM ngoài nhà nước có mức tăng trưởng LNST đáng chú ý .Ở chiều ngược lại các ngân
            hàng quốc doanh như VCB, BID đều có mức tăng trưởng lợi nhuận sau thuế âm.Các ngân hàng
            có lợi nhuận sau thuế Quý 01.2020 tăng so với cùng kỳ năm ngoái là: ACB (13%), TPB (19%)
            với giá trị lần lượt là: 1,537.053 triệu đồng, 809.589 triệu đồng. Các ngân hàng có lợi nhuận sau
            thuế Quý 01.2020 giảm so với cùng kỳ năm ngoái là: BID (-29%) và VCB (-4%)
            Tính đến cuối năm 2020, lợi nhuận của các ngân hàng niêm yết đạt 279,880 tỷ đồng, tăng 11.8%
            so với cùng kỳ năm ngoái. Tăng trưởng lợi nhuận ròng tăng được đóng góp chính bởi các ngân
            hàng thương mại tư nhân, với mức tăng 17.5% YoY lên tổng cộng 172,217 tỷ đồng. Ở chiều
            ngược lại, các NHTM có yếu tố nhà nước chỉ ghi nhận mức tăng trưởng vỏn vẹn 3.8% YoY lên
            107,663 tỷ đồng.Trong năm 2021, tăng trưởng lợi nhuận của nhóm ngân hàng thương mại có yếu
            tố nhà nước sẽ vượt trội so với nhóm NHTM tư nhân. Đà tăng trưởng lợi nhuận của nhóm NHTM
            nhà nước sẽ được hỗ trợ bởi việc cải thiện hệ số NIM mạnh mẽ và chi phí trích lập dự phòng ổn
            định hơn.Các NHTM tư nhân theo dự báo vẫn sẽ duy trì tốc độ tăng trưởng lợi nhuận từ 20-25%
            trong năm 2021.11.""")
            st.write("""- Trong Q4/2020 và 3 tháng đầu năm 2021, các ngân hàng đồng loạt ghi nhận lợi nhuận sau thuế
            tăng trưởng mạnh. Lợi nhuận các ngân hàng tăng chủ yếu từ các yếu tố: (i) Thu nhập lãi thuần
            vẫn tăng nhờ tín dụng vẫn duy trì mức tăng và biên độ lãi ròng (NIM) tiếp tục nới rộng ở phần
            lớn các ngân hàng. (ii) Lãi dịch vụ của nhiều ngân hàng tăng mạnh. Trong đó, một số ngân hàng
            chủ yếu nhờ lợi nhuận đến từ Bancarsurrance trong bối cảnh phải giảm nhiều loại phí dịch vụ
            khác nhằm hỗ trợ các doanh nghiệp và người dân gặp nhiều khó khăn do ảnh hưởng của dịch
            bệnh COVID-9. Nhiều ngân hàng trong nhóm quy mô trung bình và lớn chạy đua phát triển các
            dịch vụ digital banking và triển khai eKYC. (iii) Một số ít ngân hàng có lãi đầu tư cao từ trái
            phiếu doanh nghiệp và trái phiếu tổ chức tín dụng. (iv) Tỷ lệ Chi phí trên lợi nhuận hoạt động
            (CIR) của nhiều ngân hàng giảm do tốc độ tăng trưởng của lợi nhuận cao hơn chi phí hoạt
            động.VCB có lợi nhuận sau thuế đạt 10,858 tỷ đồng với mức tăng trưởng lợi nhuận sau thế là
            24%YoY và trong quý 2/2021 và giảm một cách rõ rệt vào Q2/2021, ACB đạt mức 2,475 với
            mức tăng trưởng 66% YoY, SCB có lợi nhuận sau thuế đạt 416 tỷ đồng với mức tăng trưởng
            561% YoY.""")
    if rad== 'Tăng trưởng tín dụng':
        st.subheader('Phân tích tăng trưởng tín dụng')
        with st.expander("Lý thuyết:"):
            st.write('- Về lý thuyết, tín dụng là mối quan hệ giữa người vay và người cho vay. Trong đó, người cho vay có nhiệm vụ chuyển giao quyền sử dụng tiền hoặc hàng hóa cho vay cho người đi  vay trong thời gian nhất định nào đó. Người đi vay có nghĩa vụ phải trả đủ số tiền hoặc hàng hóa đã đi vay khi đến hạn, có thể kèm hoặc không kèm theo lãi. Tín dụng ngân hàng là mối quan hệ tín dụng giữa ngân hàng (NH), các tổ chức tín dụng (TCTD) với các doanh nghiệp hay các cá nhân (bên đi vay). Trong đó, NH hay TCTD sẽ chuyển giao tài sản cho bên đi vay sử dụng trong một thời gian nhất định, khi đến hạn, bên đi vay phải hoàn trả cả gốc lẫn lãi cho TCTD.')
            st.write('- Tăng trưởng tín dụng là tổng tín dụng của toàn hệ thống ngân hàng trong năm nay sẽ lớn hơn năm trước. Ví dụ: Tăng trưởng tín dụng tăng 20%, có nghĩa rằng tổng tín dụng của toàn hệ thống ngân hàng năm nay sẽ cao hơn so với năm trước là 20%.')

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
            width=750,
            height=400)
        st.plotly_chart(cg)

        with st.expander("Đánh giá:"):
            st.write("""- Đến đầu năm 2019, hầu hết các ngân hàng được niêm yết trên sàn chứng khoán tiêu biểu như
            Vietcombank, Viettinbank, BIDV, Saccombank, TP Bank, ACB...đều được cấp hạn mức tín
            dụng cho cả năm khoảng 12% đến 13% YoY, thấp hơn hạn mức ban đầu đặt ra so với năm 2018 là
            14% đến 15% YoY. Có riêng trường hợp của ngân hàng Viettinbank là giữ hạn mức 7%, do hạn chế
            về mức đủ vốn. Sau đó đã có một vài ngân hàng xin nâng hạn mức tín dụng lên 17% đến 18% YoY
            trong quý 4/2019. Mức điều chỉnh + 1 về tăng trưởng tín dụng cho khối ngân hàng TMCP (chiếm
            20% thị phần) giúp tăng trưởng tín dụng toàn hệ thống tăng 0.19%. Trong khi đó, đối với khối
            ngân hàng quốc dân (chiếm 48% tổng thị phần) thì chỉ có ngân hàng Vietcombank xin nâng hạn
            mức tín dụng từ 13% lên 15%.""")
            st.write('''- Tăng trưởng tín dụng trong các giai đoạn của năm 2019, khi ảnh hưởng của dịch COVID lên
            Việt Nam chưa lớn ước tính khoảng 13.5% đến 13.7% YoY (có thấp hơn so với năm 2018 một chút
            13.89%, nhưng không đáng kể) bù lại thì tổng phương tiện thanh toán trong năm 2019 lại tăng
            lên một chút.''')
            st.write('''- Trong 6 tháng đầu năm 2020 (quý 1, quý 2) các ngân hàng có sự tăng trưởng tín dụng trung
            bình là +14.2% . Mức tăng trưởng tín dụng này có sự phân hóa giữa các ngân hàng quốc doanh
            ( VCB, BID, CTG) , ở quý 1 thì cả 3 ngân hàng quốc doanh đều có mức tăng trưởng trưởng giảm
            sâu so với năm 2019. Tuy nhiên, các ngân hàng tư nhân lại đạt mức tăng trưởng tín dụng cao hơn
            6.9% YTD.''')
            st.write('''- Nhìn chung trong giai đoạn này, các ngân hàng Việt Nam đã ít nhiều bắt đầu phải chịu ảnh
            hưởng cuả đại dịch COVID khi tăng trưởng tín dụng đã có dấu hiệu suy yếu, tăng trưởng tín
            dụng trung bình chỉ đạt 3.65%YTD, chỉ bẳng một nửa 7.4%, so với nửa đầu năm 2019. Khách
            hàng doanh nghiệp lớn và trái phiếu doanh nghiệp là động lực tăng trưởng chính với tăng trưởng
            cao nhất là 6.1%YTD có thể kể đến các ngân hàng TP Bank và Saccombank, tăng trưởng cho
            vay cá nhân đạt 2.9%, dẫn đầu là ngân hàng VCB, tăng trưởng cho vay doanh nghiệp xếp vị trí
            thấp nhất cũng đã đạt 1.83%.''')
            st.write('''- Đến 6 tháng cuối năm 2020 (quý 3, quý 4) thì tổng tăng trưởng tín dụng của các ngân hàng đã
            có dấu hiệu khởi sắc khi tăng nhẹ 3.7%YTD so với mức 3.65%YTD trong 6 tháng đầu năm 2020
            và con số này cũng chỉ bằng một nửa 7.7%YTD của năm 2019. Theo thống kế từ dữ liệu tài
            chính thu thập được thì ước tính mức tăng trưởng tín dụng của các ngân hàng trong năm 2020
            chỉ đạt khoảng 7.5% đến 8.5% YTD thấp hơn mục tiêu tăng trưởng tín dụng ban đầu mà các ngân
            hàng đư ra là 11% đến 12% YTD. Nhu cầu tín dụng có theetr suy yếu do cả nước đang đối mặt với
            làn sóng đại dịch COVID 19 lần thứ hai trong khi các ngân hàng có thể không hạ mức tăng4
            trưởng tín dụng. Cho vay khách hàng doanh nghiệp lớn và trái phiếu doanh nghiệp có thể là động
            lực chính cho tăng trưởng tín dụng, trong khi tăng trưởng tín dụng mảng khách hàng cá nhân
            không còn dồi dào và mạnh mẽ như trước. Mức tăng trưởng tín dụng giữa khách hàng cá nhân
            và khách hàng doanh nghiệp có thể sẽ được đảo ngược sau khi đại dịch COVID 19 đã ổn định.''')
            st.write("""- Sang đến nửa đầu năm 2021, nhìn chung tổng hạn mức tăng trưởng tín dụng của các ngân hàng
            đều có dấu hiệu tăng trưởng trở lại nhưng mức tăng trưởng tín dụng cũng còn khá khiêm tốn,
            chưa có tăng đột biến lắm. Cho vay doanh nghiệp vẫn giữ vững đà tăng trưởng tốt trong khi cho
            vay khách hàng cá nhân đang có dấu hiệu phục hổi, tiêu biểu là BIDV và VCB. Trong khoảng
            thời gian này ngân hàng nhà nước đã nới hạn mức tín dụng đối với nhiều Ngân hàng thương mại
            cổ phần. """)
    if rad == 'Thu nhập của ngân hàng':
        st.subheader('Phân tích thu nhập của ngân hàng')
        with st.expander("Lý thuyết:"):
            st.write('- Về lý thuyết, Thu nhập ròng là khoản thu nhập trước thuế trừ đi khoản thuế thu nhập phải nộp cho ngân sách nhà nước, ngân sách địa phương của năm đó. (Thu nhập trước thuế là sự chênh lệch giữa tổng thu nhập hoạt động và tổng chi phí).')
        ltc = go.Figure(data=[
            go.Bar(name='ACB', x= Quarter, y= a3),
            go.Bar(name='SCB', x= Quarter, y= s3),
            go.Bar(name='BID', x= Quarter, y= b3),
            go.Bar(name='TPB', x= Quarter, y= t3),
            go.Bar(name='VCB', x= Quarter, y= v3),
            go.Bar(name='VTB', x= Quarter, y= vt3),
        ])
        ltc.update_layout(title='Thu nhập của các ngân hàng qua các quý từ 2019-2021',yaxis_title='Thu nhập',
                        xaxis_title='Qúy 1 2019 - Qúy 2 2021',barmode='group')

        ltc.update_layout(
        autosize=False,
        width=750,
        height=400)
        st.plotly_chart(ltc)
        with st.expander("Đánh giá:"):
            st.write('''- Thông qua biểu đồ thể hiện, nhìn chung mức thu nhập ròng (hay còn gọi thu nhập ngoài lãi)
            của các ngân hàng vẫn tăng trưởng ở mức ổn định từ khi dịch COVID bắt đầu xuất hiện ở Việt
            Nam cho đến khi dịch đạt đỉnh. Trong năm 2019 thì mức thu nhập ròng ở một số ngân hàng tiêu
            biểu có một số điểm bất thường từ các nợ xấu đã xử lí, từ phí phân phối bảo hiểm qua kênh ngân
            hàng ( phí Bancassurance) và lợi nhuận từ bán trái phiếu chính phủ đều giảm nhưng thu nhập
            ròng từ phí giao dịch ngân hàng lại có khả năng bù đắp được giảm đó cho nên mức biến động
            của các ngân hàng hầu như không bị ảnh hưởng. Tuy nhiên, trong năm 2019 các ngân hàng có
            mức thu nhập ròng tăng trưởng hơn so với cùng kì năm 2018 là nhờ vào thu nhập từ hoa hồng
            bán bảo hiểm và thu nhập từ dịch vụ thẻ. Đến năm 2020 thì mức thu nhập ròng này lại có dấu
            hiệu tăng trưởng khá, tổng thu nhập ròng này tăng hơn so với năm 2019 là nhờ vào các hoạt động
            kinh doanh ngoại hối và đầu tư chứng khoán, tiêu biểu là giá cổ phiếu của ngân hàng BIDV,
            VCb, ACB đã có lúc đạt đỉnh và thu về cho ngân hàng một lượng thu nhập khổng lồ. Trong khi
            đó thì tăng trưởng thu nhập từ phí giao dich lại chỉ nằm ở mức khiêm tốn và từ thu nhập từ nợ
            xấu đã xóa giảm. Điều đáng quan tâm là nhiều người cho rằng trong lúc đỉnh dịch bùng phát thì
            khả năng các ngân hàng sẽ bị giảm thu nhập ròng, nhưng điều đó lại không xảy ra và ngược lại
            là tăng mạnh. Nhìn chung, theo đánh giá của các chỉ số cho thấy thu nhập từ các dịch vụ thanh
            toán, tài trợ thương mại, Bancassurence và kiều hối đều khôi phục mạnh mẽ nhờ nhu cầu bị dồn
            nén sau thời gian giãn cách xã hội kéo dài.''')
            st.write('''- Nhiều ngân hàng cho biết, nguyên nhân trong điều kiện dịch bệnh, khách hàng ngại giao dịch
            trực tiếp và cũng không thể ra ngoài do giãn cách xã hội suốt thời gian dài, vì vậy các ngân hàng
            đã đẩy mạnh các dịch vụ ngân hàng số, số hóa các giao dịch. Theo đó, nhiều chương trình ưu15
            đãi, miễn, giảm, hỗ trợ phí cho khách hàng giao dịch trực tuyến cũng được triển khai. Điều này
            không chỉ hỗ trợ kịp thời cho khách hàng mà còn mang lại lợi ích cho chính ngân hàng, bù đắp
            được khoản lợi nhuận đã hy sinh do việc giảm phí. Chính vì thế, mà trong đợt bùng dịch thứ hai
            này một số ngân hàng không chỉ tăng thu nhập ròng mà còn huy động được khoản tiền gửi lớn,
            đem lại lợi ích cho kinh doanh.''')
    if rad== 'Thu nhập từ dịch vụ':
        st.subheader('Phân tích thu nhập từ dịch vụ')
        with st.expander("Lý thuyết:"):
            st.write('Thu nhập từ hoạt động dịch vụ:')
            st.write('a) Thu từ dịch vụ thanh toán gồm: Thu từ cung cấp dịch vụ thẻ, ngân hàng điện tử; thu mở tài khoản thanh toán, cung cấp phương tiện thanh toán cho các quỹ tín dụng nhân dân thành viên và các khách hàng không phải là quỹ tín dụng nhân dân thành viên.')
            st.write('b) Thu từ dịch vụ ngân quỹ')
            st.write('c) Thu từ nghiệp vụ ủy thác và đại lý.')
            st.write('d) Thu từ hoạt động dịch vụ khác gồm:')
            st.caption('- Thu từ cung ứng các dịch vụ tư vấn tài chính, ngân hàng và đầu tư.')
            st.caption('- Thu từ cung ứng sản phẩm dịch vụ mới phục vụ cho hoạt động của quỹ tín dụng nhân dân thành viên và phục vụ phát triển lợi ích cộng đồng trên địa bàn.')
            st.caption('- Thu từ hoạt động đại lý trong các lĩnh vực ngân hàng, kinh doanh bảo hiểm.')
            st.caption('- Thu từ các dịch vụ khác theo quy định của pháp luật.')
        nfci = go.Figure()
        nfci.add_trace(go.Scatter(x=Quarter, y=acb_nfci,
                            mode='lines+markers',
                            name='ACB'))
        nfci.add_trace(go.Scatter(x=Quarter, y=bid_nfci,
                            mode='lines+markers',
                            name='BIDV'))
        nfci.add_trace(go.Scatter(x=Quarter, y=vcb_nfci,
                            mode='lines+markers',
                            name='VCB'))
        nfci.add_trace(go.Scatter(x=Quarter, y=vtb_nfci,
                            mode='lines+markers',
                            name='VTB'))
        nfci.add_trace(go.Scatter(x=Quarter, y=scb_nfci,
                            mode='lines+markers',
                            name='SCB'))
        nfci.add_trace(go.Scatter(x=Quarter, y=tpb_nfci,
                            mode='lines+markers',
                            name='TPB'))
        nfci.update_layout(title='Thu nhập từ hoạt động dịch vụ của các ngân hàng qua các quý từ 2019-2021',yaxis_title='Thu nhập từ dịch vụ',
                        xaxis_title='Quý 2019 - Quý 2021')
        nfci.update_layout(
        autosize=False,
        width=750,
        height=400)
        st.plotly_chart(nfci)
        with st.expander("Đánh giá:"):
            st.write('''- Tỷ trọng đóng góp của thu nhập dịch vụ trong tổng thu nhập hoạt động của các ngân hàng tăng
            10% trong năm 2019 và 13,8% trong năm 2020. Kết thúc quý I/2019, báo cáo của nhiều ngân
            hàng cũng ghi nhận xu hướng tăng thu dịch vụ khả quan.''')
            st.write('''- Theo báo cáo tài chính hợp nhất quý I/2019 của Ngân hàng Thương mại cổ phần Công thương
            Việt Nam (2019) cho thấy, lãi từ hoạt động dịch vụ của ngân hàng này tăng đột biến 64%, đạt
            969 tỷ đồng. Hoạt động dịch vụ cũng đóng góp tới 1.069 tỷ đồng vào tổng thu nhập hoạt động
            của Ngân hàng Thương mại cổ phần Ngoại thương Việt Nam, tăng 21%, so với cùng kỳ và là
            nguồn thu riêng lẻ lớn thứ hai của ngân hàng này sau tín dụng.''')
            st.write('''- Có thể thấy, phần lớn các ngân hàng hiện nay đều đã có những kế hoạch nhằm đa dạng hoá
            nguồn thu từ dịch vụ, giảm gánh nặng thu tín dụng, tạo tỷ lệ hợp lý giữa tín dụng và phi tín dụng.
            Tăng thu từ dịch vụ là xu hướng đúng đắn trong bối cảnh các ngân hàng đang phải nỗ lực đáp
            ứng chuẩn Basel II (Basel II là phiên bản thứ hai của Hiệp ước Basel, trong đó đưa ra các nguyên
            tắc chung và các luật ngân hàng của ủy ban Basel về giám sát ngân hàng.''')
            st.write('''- Riêng năm 2020, hoạt động dịch vụ phi tín dụng đã đạt mức 11,05% trong tổng thu nhập của
            các ngân hàng thương mại''')
            st.write('''- Trong nửa đầu năm 2021, dù chịu ảnh hưởng tiêu cực từ dịch bệnh, song, các ngân hàng vẫn
            báo lợi nhuận tăng trưởng so với cùng kỳ. Các chính sách hỗ trợ cơ cấu lại nợ, kéo dài thời gian
            trích lập dự phòng rủi ro… đã phần nào góp phần làm lợi nhuận ngân hàng tăng, nhưng chủ yếu
            vẫn là do chính các ngân hàng đã thích nghi dần với sự thay đổi của nền kinh tế, tăng mạnh được
            nguồn thu kể cả thu nhập chính và thu nhập phi tín dụng.Theo đó, tốc độ tăng trưởng nguồn thu
            chính trong 6 tháng đầu năm 2021 tại đa số các ngân hàng đạt bình quân từ 30-50%, so với cùng
            kỳ năm trước.Riêng trường hợp của SCB, là nhà băng duy nhất báo lỗ trong hoạt động chính,
            nguyên nhân là do trong quý 2, tốc độ giảm của chi phí lãi (-1%) không nhanh bằng tốc độ giảm
            của thu nhập lãi và các khoản thu nhập tương tự (-15%).Xét về cơ cấu thu nhập, tỷ trọng nguồn
            thu ngoài lãi dù có cải thiện, nhưng vẫn chiếm tỷ trọng từ 10-30% thu nhập hoạt động của các
            ngân hàng, còn lại là thu nhập từ hoạt động chính. Trừ trường hợp của SCB khi nguồn thu chính
            báo lỗ, 100% thu nhập đều đến từ thu ngoài lãi.''')
            st.write('''- Thu từ dịch vụ thường chiếm tỷ trọng nhiều nhất trong cơ cấu thu nhập phi tín dụng của các ngân
            hàng. tổng thu nhập phi tín dụng tại 28 ngân hàng tăng 38%, so với cùng kỳ, trong khi thu nhập
            lãi thuần chỉ tăng 33%.Tính riêng thu nhập từ dịch vụ tăng đến 58%, so với cùng kỳ.lợi nhuận
            của ACB tăng trưởng nửa đầu năm 2021 ngoài nhờ tăng trưởng tín dụng 19-20%, biên lãi ròng
            nới rộng và còn nhờ hoạt động bán chéo bảo hiểm sau khi ký kết độc quyền sản phẩm nhân thọ
            của Sunlife Việt Nam. Doanh thu từ thu nhập phí bảo hiểm nửa đầu năm của ACB đạt 1,300 tỷ
            đồng, tăng 70%, so với cùng kỳ năm trước, với 853 tỷ đồng đến từ mảng Bancassurance.TPBank
            cũng ghi nhận tăng mạnh thu từ dịch vụ (gấp 2.2 lần), thu về 695 tỷ đồng tiền lãi trong nửa đầu
            năm, chủ yếu nhờ tăng mạnh thu phí hoạt động thanh toán (+38%), tăng thu phí dịch vụ kinh
            doanh, dịch vụ bảo hiểm và tư vấn (+94%).Một điểm đáng chú ý trong cơ cấu thu nhập phi tín
            dụng của các ngân hàng trong nửa đầu năm nay là nguồn thu từ đầu tư chứng khoán sụt giảm so
            với các nguồn thu nhập khác hoặc gần như không ghi nhận. Theo giải trình của Vietcombank,
            thu nhập từ lãi tiền gửi giảm và không ghi nhận lãi từ chứng khoán đầu tư chủ yếu do lãi suất
            liên ngân hàng có xu hướng giảm do tình trạng thanh khoản của hệ thống ngân hàng vẫn dồi dào
            trong khi tình hình dịch Covid-19 trở lại căng thẳng và ảnh hưởng nghiêm trọng, làm giảm năng
            lực hấp thụ vốn của nền kinh tế. Đồng thời, trong thời gian qua một số khoản trái phiếu TCTD17
            của Vietcombank đáo hạn nhưng chưa được đầu tư thay thế hoặc được đầu tư thay thế bằng trái
            phiếu có mức lãi suất thấp hơn.''')
    if rad== 'ROA - ROE':
        st.subheader('Phân tích ROA - ROE')
        with st.expander("Lý thuyết:"):
            st.write('- Về lý thuyết, ROA (Return on Assets) là chỉ số thể hiện tỷ suất sinh lời trên tài sản. Chỉ số này thể hiện tỷ lệ giữa lợi nhuận so với tài sản được đem vào hoạt động sản xuất kinh doanh nhằm đánh giá hiệu quả trong việc sử dụng tài sản của doanh nghiệp.')

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
        width=750,
        height=400)
        st.plotly_chart(roa)
        with st.expander("Đánh giá:"):
            st.write("""* Những tháng đầu năm 2019 ,hầu hết những ngân hàng có ROA cao là những ngân hàng có quy
            mô vừa và nhỏ trong khi các ngân hàng “gốc” Nhà nước có hệ số ROA khá thấp so với bình quân
            ngành. Ngoại trừ ROA của VCB đạt 1.39% thì 2 "ông lớn" còn lại là BIDV (BID, 0.59%) và
            VietinBank (VTB, 0.48%) đều ở mức khá thấp. Xét đến hiệu quả sinh lời, ROE của VTB thường
            duy trì trong khoảng 12 - 13%, thấp hơn nhiều so với các ngân hàng vừa và lớn khác. Một lý do
            cho mức ROE thấp là do chiến lược của ngân hàng tập trung vào hoạt động cho vay doanh nghiệp,
            vốn có lợi suất thấp hơn so với cho vay cá nhân, đồng thời ngân hàng cần thời gian để giải quyết
            các bất cập do bộ máy quản lý trước để lại. Tuy nhiên, lợi suất của của CTG đã cải thiện trong
            năm 2020, đạt 17% và là ngân hàng quốc doanh duy nhất ghi nhận tỷ lệ khả năng sinh lời tăng
            so với năm 2019. Chúng tôi cho rằng điều này đạt được là nhờ nỗ lực của ngân hàng trong việc
            kiểm soát hoạt động cho vay và chi phí hoạt động. Trong giai đoạn 2021 - 2023, chúng tôi dự
            báo ROA sẽ duy trì lần lượt ở mức 1,2% và 18% nhờ dòng thu nhập từ hoạt động bancassurance
            và áp lực giải quyết nợ xấu giảm.""")

        with st.expander("Lý thuyết:"):
            st.write('- Về lý thuyết, ROE (Return on Equity) là chỉ số thể hiện tỷ suất sinh lời trên vốn chủ sở hữu. Chỉ số này thể hiện tỷ lệ giữa lợi nhuận so với vốn chủ sở hữu mà doanh nghiệp sử dụng vào hoạt động của doanh nghiệp nhằm đánh giá hiệu quả trong việc sử dụng vốn.')
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
        width=750,
        height=400)
        st.plotly_chart(roe)
        with st.expander("Đánh giá:"):
            st.write("""* 9T.2019 Tỷ lệ ROE biến động, nhóm ngân hàng đã đáp ứng chuẩn Basel II như VCB TPB
            BIDV ACB,... có mặt bằng chung ROE cao hơn nhóm còn lại. Điều này là hợp lý khi các ngân
            hàng này có mức tăng trưởng tín dụng và lợi nhuận tốt hơn giúp cải thiện, duy trì ROE ở mức
            cao hơn trung bình ngành. tỷ lệ ROE được cải thiện so với cuối năm 2018 và vẫn ở mức cao so
            với trung bình ngành.""")
            st.write('''- Câu chuyện hồi phục trong năm 2021 đã phản ánh một phần vào giá. Đối với các ngân hàng
            trong phạm vi nghiên cứu của chúng tôi, với ROE trung bình là 18,6%. Năm 2021, ước tính ROE
            trung bình là 17,2%. Theo quan điểm của chúng tôi, điều này cho thấy diễn biến cổ phiếu ngân
            hàng đã phản ánh một phần câu chuyện phục hồi năm 2021, do ROE trung bình toàn hệ thống
            đã cao hơn mức trước Covid. Mặc dù vậy, cổ phiếu vẫn còn khả năng tăng giá. Hiện tại, chúng
            tôi chưa nhận thấy bất kỳ yếu tố tác động cụ thể nào để đánh giá lại ngành và duy trì xếp hạng
            Khả quan.Chúng tôi nhận thấy cơ hội ở các ngân hàng có mức định giá thấp hơn (hoặc cao hơn
            một chút) so với mức trước Covid, bao gồm: VCB, TCB, BID, VTB. Trong số đó, VCB và BID
            vẫn gặp thách thức về vốn, với dư địa phát hành trái phiếu cấp 2 hạn chế.''')
    if rad== 'Tiền gửi ngân hàng':
        st.subheader('Tiền gửi trong các ngân hàng')
        with st.expander("Lý thuyết:"):
            st.write('''- Về lý thuyết,Tiền gửi ngân hàng là tiền được gửi trong các tài khoản ở ngân hàng (theo nghĩa
            đơn giản). Trên thực tế, nó chính là số liệu về khoản nợ của một ngân hàng đối với người gửi
            tiền. Loại tiền này phát sinh từ vai trò trung gian tài chính của ngân hàng. Tiền gửi được giữ
            trong nhiều tài khoản khác nhau ở điều kiện sử dụng hay rút tiền ra.''')

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
        width=750,
        height=400)
        st.plotly_chart(dtc)
        with st.expander("Đánh giá:"):
            st.write("""- Theo đánh giá ngân hàng Nhà nước, tính đến 6 tháng đầu năm 2020, tổng phương tiện thanh
            toán tăng 3,7%, so với cuối năm 2019, đạt 12,558 triệu tỉ đồng, trong đó tiền gửi dân cư tăng
            2,6%, đạt 5,275 triệu tỉ đồng (mức tăng thấp nhất trong vòng 9 năm trở lại đây) và tiền gửi tổ
            chức kinh tế tăng 3,26%, đạt 5,036 triệu tỉ đồng.""")
            st.write('''- Các năm trước, tốc độ tăng trưởng tiền gửi dân cư ở mức khá cao và có xu hướng giảm dần
            những năm gần đây. Chẳng hạn, tháng 5.2012 tăng gần 16%, qua tháng 5.2013 tăng 14,26% và
            năm 2014 tăng 9,49%, năm 2015 tăng 8,31%, năm 2016 tăng 11,04%, năm 2017 tăng 9,39%,
            năm 2018 tăng 7,5%, năm 2019 tăng 6,84%, qua năm 2020 tăng 4% và nay còn 2,6%.''')
            st.write('''- Ngược lại, số liệu tiền gửi thanh toán cá nhân (tài khoản thanh toán của cá nhân) trong quý
            1/2021 lại tăng khá mạnh so với những năm trước. Số lượng tài khoản quý 1/2021 đạt 104,189
            triệu tài khoản với dư nợ 741.378 tỉ đồng, tăng 264.855 tỉ đồng so với cùng kỳ năm ngoái. Để lí
            giải cho điều này ,cũng chính do tác động của đại dịch COVID 19 mà người dân phải chuyển
            qua thanh toán trực tuyến nhiều thay vì dùng tiền mặt. Đồng thời tỉ lệ người dân mất việc nhiều
            nên mọi khoản tích góp gửi ngân hàng bây giờ họ dùng cho mục đích chi tiêu cá nhân và không
            còn khoản nào khác để gửi ngân hàng. Khi ngân hàng hỗ trợ phí và miễn phí chuyển tiền giao
            dịch, số tiền nhàn rỗi của khách hàng sẽ được gửi vào tài khoản ngân hàng nhiều hơn. Một phần,
            khách hàng không lo mất phí khi chuyển tiền mà phần khác để phục vụ chi tiêu trực tuyến trong
            thời gian dịch bệnh. Không chỉ thế, chính sách miễn, giảm phí giao dịch còn giúp các ngân hàng
            huy động được nguồn vốn giá rẻ thông qua nguồn tiền gửi không kỳ hạn (CASA). Khi thói quen
            thanh toán trực tuyến gia tăng, lượng tiền gửi trong tài khoản cũng sẽ tăng theo, nhờ đó các ngân7
            hàng có thể tiếp cận nguồn vốn giá rẻ này để cho vay, từ đó góp phần gia tăng biên lợi nhuận
            (NIM).''')
            st.write('''- Ngân hàng Nhà nước cho biết, tính đến tháng 4/2021, tiền gửi của khách hàng tại hệ thống các
            tổ chức tín dụng (TCTD) ở mức trên 5,26 triệu tỷ đồng, chỉ tăng 2,34%, so với cuối năm 2020.
            Đây là mức tăng trưởng thấp nhất so với cùng kỳ nhiều năm trước trong lịch sử dữ liệu thống kê
            được công bố.''')
            st.write('''- Trước đó, cùng kỳ những năm 2013 và 2014, khi lãi suất huy động còn ở mức khá cao, từ 7-
            9%/năm thì tăng trưởng tiền gửi của dân cư tại các TCTD từng lên tới 13,55% và 9,83%. Tuy
            nhiên, hai năm gần đây, tiền gửi dân cư lần lượt chỉ còn tăng 3,37% tại tháng 4/2020 và thấp nhất
            là tháng 4/2021 chỉ tăng 2,34%.
            Gửi tiết kiệm vào ngân hàng trước nay đều được đánh giá là kênh đầu tư an toàn, nhất là trong
            thời điểm dịch bệnh nhưng với mức lãi suất tiền gửi thấp như hiện nay đã khiến dòng tiền tích
            lũy của người dân dịch chuyển sang các kênh đầu tư khác.
            Theo thống kê, mặt bằng lãi suất đã giảm từ 1,5% đến 2,5%. Hiện tại, lãi suất huy động kỳ hạn
            1 tháng tại một số ngân hàng chỉ còn 3,3%/năm, thấp nhất trong 10 năm trở lại đây.''')

    if rad == 'Kết luận':
        st.header('Kết luận')
        st.markdown('''- Do tác động của đại dịch Covid-19, nền kinh tế Việt Nam nói chung và lĩnh vực tài chính, ngân
        hàng nói riêng không tránh khỏi những tác động tiêu cực, mặc dù Chính phủ và Ngân hàng Nhà
        nước Việt Nam (NHNN) đã đưa ra nhiều giải pháp nhằm khắc phục những tác động tiêu cực đó.
        Đối với thị trường tài chính, ngân hàng.''')
        st.markdown('''- Ảnh hưởng của đại dịch Covid-19 gây ra tâm lý tiêu cực trong và sau đại dịch khiến cho khách
        hàng tiêu dùng và nhà đầu tư có trạng thái tâm lý trì hoãn tiêu dùng, không có nhu cầu vay vốn
        và đầu tư, điều này ảnh hưởng gián tiếp đến các dịch vụ ngân hàng như Internet banking, giao
        dịch các sản phẩm ngân hàng… ảnh hưởng lợi nhuận ròng từ tín dụng và phi tín dụng của ngân
        hàng.''')
        st.markdown('''- Sau đại dịch Covid-19, sự phá sản của các doanh nghiệp có thể tạo ra khủng hoảng nợ, là tiền
        đề cho nợ xấu ngân hàng tăng và hệ lụy ảnh hưởng những “đổ vỡ” trong hệ thống tài chính.''')

    if rad == 'Lời cảm ơn':
        st.balloons()
        st.header('Lời cảm ơn')
        st.markdown('Lời đầu tiên, nhóm chúng em xin chân thành cảm ơn Thầy Nguyễn Phúc Sơn đã tận tình đồng hành và hướng dẫn nhóm để nhóm hoàn thành bài giữa kì này.')
        st.markdown('Xin chân thành cảm ơn Trung tâm Nghiên cứu Kinh tế và Tài chính Trường Đại học Kinh tế - Luật đã nhiệt tình hỗ trợ và cung cấp cho nhóm nguồn dữ liệu chuẩn xác nhất để hoàn thiện bài giữa kì.')
        st.markdown('Cuối cùng nhóm xin gửi lời cảm ơn đến cá bạn lớp Data Visualization đã chia sẻ và giúp đỡ nhóm.')
        st.markdown('Xin chân thành cảm ơn đến tất cả mọi người. Chúc sức khỏe và bình an!')
    
