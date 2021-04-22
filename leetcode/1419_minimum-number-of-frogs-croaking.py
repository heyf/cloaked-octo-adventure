# https://leetcode.com/problems/minimum-number-of-frogs-croaking

class Solution:
    def minNumberOfFrogs(self, croakOfFrogs: str) -> int:
        min_frog = 0
        status = [0,0,0,0,0]
        cindex_dict = {
            "c": 0,
            "r": 1,
            "o": 2,
            "a": 3,
            "k": 4
        }
        for c in croakOfFrogs:
            cindex = cindex_dict.get(c)
            if cindex == 0:
                status[cindex] += 1
                continue
            if status[cindex-1] == 0:
                return -1
            status[cindex-1] -= 1
            status[cindex] += 1
            min_frog = max(min_frog, sum(status[:4]) if cindex < 4 else 1 + sum(status[:4]))
        if sum(status[:4]) > 0:
            return -1
        return min_frog

sl = Solution()
# croakOfFrogs = "croakcroak"
# croakOfFrogs = "crcoakroak"
# croakOfFrogs = "croakcrook"
# croakOfFrogs = "croakcroa"
croakOfFrogs = "ccccccccrcccrcccccccccrccccccrccccccrcccccccccccccccrccccrcccccccccccccrccrcrccccccccccrrrcccrcccrrcccrrccccrccccccccccccrcrrcrccccoccccrcccrcccccrcrccccrrrccrcrcccrcorcccccccrrccccccrrrrrcoocoocorcocrrcorccoccccrrcccrcrcacorcrocccrcrrrocccracrorrrrccococcccocrcrrrrrrrocarrrrcoccrorrrccckroccocrroacoccrrororrocrocaocrcrccccccrrooocoocorrrcrarcocrkcorrrrrorrraccrrrooarrraoccroaacrroccraaoraoorroorccokooaorcoocaroororrrocrroccrcrraookoarorrkcrrcoorrorackroooroarcacrorccaroaacorcraccrcocorrroorcraoooroaorccoorrroocokaaooaooarrrrocarcarkraroooorkrcoakarorraoarrooacccrrorkcroorrcockkaaoraororoccckraoccooackorarroookraooaarrrraacrarkkkrcaokaroroakarroorooorrorkkrkaraaocaackroorarocoackarracckkoorraccrrooaaokaooaorokoaaaoaaoarkarackooaaccoraaaooaokrckrooocraakkkaarraarrkoaarraaorrakcaaakockkkcookccaaaacrorooaokkorooaarkrkookkcakooaarocokrkrrarrcaakrorrakrokkrorakoaroaoaaaaaakkkookrakakckaaccokkaorkakrokkrkooooaakaoaakkraokoaoorooaorkoorkoraarkaaoacarkraokoakaookcorookaokrkrracaokkooaroroarkaraokkaakakcorkrackoarkakarkroackakcoarakaakrkarkcrkkaookkaakkkaacraakokkraoaaoaakaaakokookaooorrkooakkrokooraookaoraakkaakaokarackkkkkoaakakacoakaoakokokkarkaookkaokakkoaoaraaokorkkkaoakkoaaaaokoakkkkkkaoaoaakaokakkakoaookakrokaarakaaaooaoarakookkkkkkokkkkkokaakkkaooaaokrooorarkroaaaoakkookoakaakaoaaaaaakkkkaokrokakakakkkokorcakkarkkakkkorakkcaoaaooaokkkkookkkkakrkakkakkkaokkkkkkkkkaakaaakkkkkakkakaokkakkaookkakkaakkkakaoakakkckkakakkkakkaaakakkkkkkkkkakkakroakkkkkkkaakkkkkokkokarakoakk"
ret = sl.minNumberOfFrogs(croakOfFrogs)
print(ret)
