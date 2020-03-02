from tethys_sdk.base import TethysAppBase, url_map_maker


class Resume(TethysAppBase):
    """
    Tethys app class for Resume.
    """

    name = 'Resume'
    index = 'resume:home'
    icon = 'resume/images/resume_logo.jpg'
    package = 'resume'
    root_url = 'resume'
    color = '#171117'
    description = '"This is an app that has my resume on it :)"'
    tags = '"Spare Time"'
    enable_feedback = False
    feedback_emails = []

    def url_maps(self):
        """
        Add controllers
        """
        UrlMap = url_map_maker(self.root_url)

        url_maps = (
            UrlMap(
                name='home',
                url='resume',
                controller='resume.controllers.home'
            ),
        )

        return url_maps
