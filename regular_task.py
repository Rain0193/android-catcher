from task import Task


class OpenPermissionsTask(Task):

    def __init__(self, name):
        super().__init__(name)

    def execute(self):
        self.d.adb_shell(
            "am start -a android.intent.action.MANAGE_APP_PERMISSIONS --es android.intent.extra.PACKAGE_NAME video.like")
        count = self.d(className="android.widget.Switch").count
        for i in range(0, count):
            b = self.d(className="android.widget.Switch")[i].info.get("checked")
            if not b:
                self.d(className="android.widget.Switch")[i].click()
        self.d.press("back")


class LoginTask(Task):

    def __init__(self, name, phone_number, password):
        super().__init__(name)
        self.phone_number = phone_number
        self.password = password

    def execute(self):
        self.d.app_start("video.like")
        if self.d(className="android.widget.EditText", resourceId="video.like:id/et_phone").wait(timeout=0.1):
            self.d(className="android.widget.EditText", resourceId="video.like:id/et_phone").set_text(self.phone_number)
        if self.d(className="android.widget.RelativeLayout", resourceId="video.like:id/btn_login").wait(timeout=0.1):
            self.d(className="android.widget.RelativeLayout", resourceId="video.like:id/btn_login").click()
        if self.d(className="android.widget.EditText", resourceId="video.like:id/et_passwd").wait(timeout=0.1):
            self.d(className="android.widget.EditText", resourceId="video.like:id/et_passwd").set_text(self.password)
        if self.d(className="android.widget.TextView", resourceId="video.like:id/btn_login").wait(timeout=0.1):
            self.d(className="android.widget.TextView", resourceId="video.like:id/btn_login").click()
        if self.d(className="android.widget.ImageView", resourceId="video.like:id/img_close").wait(timeout=0.1):
            self.d(className="android.widget.ImageView", resourceId="video.like:id/img_close").click()


class MainListScrollTask(Task):

    def __init__(self, name):
        super().__init__(name)

    def execute(self):
        ui = self.d(className="android.support.v7.widget.RecyclerView", resourceId="video.like:id/found_list",
                    scrollable=True)
        for i in range(10):
            ui.scroll.vert.forward(steps=10)


class DetailsListScrollTask(Task):

    def __init__(self, name):
        super().__init__(name)

    def execute(self):
        ui = self.d(className="android.view.ViewGroup", resourceId="video.like:id/detail_slide")
        for i in range(10):
            ui.scroll.vert.forward(steps=10)


class RecordVideoTask(Task):

    def __init__(self, name):
        super().__init__(name)

    def execute(self):
        self.d(className="android.widget.ImageView", resourceId="video.like:id/btn_record").click()
        self.d(className="android.widget.FrameLayout", resourceId="video.like:id/ll_entrance_shoot").click()
        self.d(className="android.widget.TextView", resourceId="video.like:id/tv_sticker").click()
        self.d(className="android.widget.ImageView", resourceId="video.like:id/iv_thumbnail_bg")[0].click()
        # self.d(className="android.view.View", resourceId="video.like:id/sticker_top_cover")[0].click()
        # 原有的点击"video.like:id/sticker_top_cover"隐藏贴纸选择列表，后发现不同版本布局有了改变
        # 有的版本找不到以上的 View，故改为点击屏幕中间的方式
        self.d.click(0.5, 0.5)
        self.d(className="android.widget.ImageView", resourceId="video.like:id/iv_record_ring").long_click(10)
        self.d(className="android.widget.ImageView", resourceId="video.like:id/iv_finish").click()
        # 录制视频之后的编辑页面用 uiautomator 实测发现有很高的捕获延迟，故以百分比的方式点击右上角的完成按钮
        self.d.click(0.948, 0.03)
        self.d(className="android.widget.FrameLayout", resourceId="video.like:id/fl_post").click()
        self.d(className="android.widget.TextView", resourceId="video.like:id/tv_done").click()


