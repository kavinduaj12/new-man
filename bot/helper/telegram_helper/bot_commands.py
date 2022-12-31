from bot import CMD_SUFFIX


class _BotCommands:
    def __init__(self):
        self.StartCommand = f'start{CMD_SUFFIX}'
        self.MirrorCommand = (f'mirror2{CMD_SUFFIX}', f'm{CMD_SUFFIX}')
        self.UnzipMirrorCommand = (f'unzipmirror2{CMD_SUFFIX}', f'uzm{CMD_SUFFIX}')
        self.ZipMirrorCommand = (f'zipmirror2{CMD_SUFFIX}', f'zm{CMD_SUFFIX}')
        self.QbMirrorCommand = (f'qbmirror2{CMD_SUFFIX}', f'qm{CMD_SUFFIX}')
        self.QbUnzipMirrorCommand = (f'qbunzipmirror2{CMD_SUFFIX}', f'quzm{CMD_SUFFIX}')
        self.QbZipMirrorCommand = (f'qbzipmirror2{CMD_SUFFIX}', f'qzm{CMD_SUFFIX}')
        self.YtdlCommand = (f'ytdl2{CMD_SUFFIX}', f'y{CMD_SUFFIX}')
        self.YtdlZipCommand = (f'ytdlzip2{CMD_SUFFIX}', f'yz{CMD_SUFFIX}')
        self.LeechCommand = (f'leech2{CMD_SUFFIX}', f'l{CMD_SUFFIX}')
        self.UnzipLeechCommand = (f'unzipleech2{CMD_SUFFIX}', f'uzl{CMD_SUFFIX}')
        self.ZipLeechCommand = (f'zipleech2{CMD_SUFFIX}', f'zl{CMD_SUFFIX}')
        self.QbLeechCommand = (f'qbleech2{CMD_SUFFIX}', f'ql{CMD_SUFFIX}')
        self.QbUnzipLeechCommand = (f'qbunzipleech2{CMD_SUFFIX}', f'quzl{CMD_SUFFIX}')
        self.QbZipLeechCommand = (f'qbzipleech2{CMD_SUFFIX}', f'qzl{CMD_SUFFIX}')
        self.YtdlLeechCommand = (f'ytdlleech2{CMD_SUFFIX}', f'yl{CMD_SUFFIX}')
        self.YtdlZipLeechCommand = (f'ytdlzipleech2{CMD_SUFFIX}', f'yzl{CMD_SUFFIX}')
        self.CloneCommand = f'clone2{CMD_SUFFIX}'
        self.CountCommand = f'count2{CMD_SUFFIX}'
        self.DeleteCommand = f'del2{CMD_SUFFIX}'
        self.CancelMirror = f'cancel2{CMD_SUFFIX}'
        self.CancelAllCommand = f'cancelall2{CMD_SUFFIX}'
        self.ListCommand = f'list2{CMD_SUFFIX}'
        self.SearchCommand = f'search2{CMD_SUFFIX}'
        self.StatusCommand = f'status2{CMD_SUFFIX}'
        self.UsersCommand = f'users2{CMD_SUFFIX}'
        self.AuthorizeCommand = f'authorize2{CMD_SUFFIX}'
        self.UnAuthorizeCommand = f'unauthorize2{CMD_SUFFIX}'
        self.AddSudoCommand = f'addsudo2{CMD_SUFFIX}'
        self.RmSudoCommand = f'rmsudo2{CMD_SUFFIX}'
        self.PingCommand = f'ping{CMD_SUFFIX}'
        self.RestartCommand = f'restart{CMD_SUFFIX}'
        self.StatsCommand = f'stats{CMD_SUFFIX}'
        self.HelpCommand = f'help{CMD_SUFFIX}'
        self.LogCommand = f'log{CMD_SUFFIX}'
        self.ShellCommand = f'shell{CMD_SUFFIX}'
        self.EvalCommand = f'eval{CMD_SUFFIX}'
        self.ExecCommand = f'exec{CMD_SUFFIX}'
        self.ClearLocalsCommand = f'clearlocals{CMD_SUFFIX}'
        self.BotSetCommand = f'bsetting{CMD_SUFFIX}'
        self.UserSetCommand = f'usetting{CMD_SUFFIX}'
        self.BtSelectCommand = f'btsel{CMD_SUFFIX}'
        self.RssListCommand = (f'rsslist{CMD_SUFFIX}', f'rl{CMD_SUFFIX}')
        self.RssGetCommand = (f'rssget{CMD_SUFFIX}', f'rg{CMD_SUFFIX}')
        self.RssSubCommand = (f'rsssub{CMD_SUFFIX}', f'rs{CMD_SUFFIX}')
        self.RssUnSubCommand = (f'rssunsub{CMD_SUFFIX}', f'rus{CMD_SUFFIX}')
        self.RssSettingsCommand = (f'rssset{CMD_SUFFIX}', f'rst{CMD_SUFFIX}')

BotCommands = _BotCommands()
