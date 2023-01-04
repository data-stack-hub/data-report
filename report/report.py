import base64
import matplotlib.pyplot as plt

class Report():
    def __init__(self):
        self.name = 'test_report'
        self.elements = []

    def header(self, content):
        content_ = '<h2>' + content + '</h2>'
        return self.elements.append(content_)
    
    def subheader(self, content):
        content_ = '<h3>' + content + '</h3>'
        return self.elements.append(content_)

    def dataframe_image(self, df):
        import dataframe_image as dfi

        dfi.export(df,"df.png")
        with open("df.png", "rb") as img_file:
            image_string = base64.b64encode(img_file.read()).decode('utf-8')
            content_ = """
            <div style=" text-align:center; padding:10px">
            <img style="margin-left: auto;margin-right: auto;" src='data:image/png;base64, {} '/>
            </div>
            """.format(image_string)
        self.elements.append(content_)
        return image_string

    def plotly_image(self, fig, width='', height=''):
        img_bytes = fig.to_image(format="jpeg", width=width, height=height)
        img_string = base64.b64encode(img_bytes).decode('utf-8')
        content_ = """
        <div style="text-align:center">
        <img style="margin-left: auto;margin-right: auto;" src='data:image/png;base64, {} '/>
        </div>
        """.format(img_string)
        self.elements.append(content_)
        return 'img_bytes'

    def image(self, image_name):
        with open(image_name, "rb") as img_file:
            image_string = base64.b64encode(img_file.read()).decode('utf-8')
            content_ = """
            <div style=" text-align:center; padding:10px">
            <img style="margin-left: auto;margin-right: auto;" src='data:image/png;base64, {} '/>
            </div>
            """.format(image_string)
        self.elements.append(content_)
        return image_string
    def chart(self, fig, width='', height='', lib='plt'):
        if lib == 'plt':
            fig
            plt.savefig('a.png')
            with open("a.png", "rb") as img_file:
                img_bytes = img_file.read()
        elif lib == 'plotly':
            img_bytes = fig.to_image(format="jpeg", width=width, height=height)
        img_string = base64.b64encode(img_bytes).decode('utf-8')
        content_ = """
        <div style="text-align:center">
        <img style="margin-left: auto;margin-right: auto;" src='data:image/png;base64, {} '/>
        </div>
        """.format(img_string)
        self.elements.append(content_)
        return 'img_bytes'

    def show(self, display='notebook'):
        if display=='notebook':
            from IPython.core.display import display, HTML
            return HTML(''.join(self.elements))
        elif display=='html':
            html_ = """
            <div style="widht:100%">{}</div>
            """.format(''.join(self.elements))
            return  html_ 
        else:
            return self.elements