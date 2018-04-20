import _main_
from task import Task


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
        self.d.click_post_delay = 1
        self.d(className="android.widget.ImageView", resourceId="video.like:id/btn_record").click()
        self.d(className="android.widget.FrameLayout", resourceId="video.like:id/ll_entrance_shoot").click()
        self.d(className="android.widget.TextView", resourceId="video.like:id/tv_sticker").click()
        self.d(className="android.widget.ImageView", resourceId="video.like:id/iv_thumbnail_bg")[0].click()
        self.d(className="android.view.View", resourceId="video.like:id/sticker_top_cover")[
            0].click()
        self.d(className="android.widget.ImageView", resourceId="video.like:id/iv_record_ring").long_click(10)
        self.d(className="android.widget.ImageView", resourceId="video.like:id/iv_finish").click()
        self.d.click(0.948, 0.03)
        self.d(className="android.widget.FrameLayout", resourceId="video.like:id/fl_post").click()
        self.d(className="android.widget.TextView", resourceId="video.like:id/tv_done").click()


_main_.main(RecordVideoTask("RecordVideo"))
