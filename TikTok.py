import requests
import json

class Tiktok():
	def __init__(self):
		self.search_id = False

	def _search_id(self):
		response = requests.get('https://www.tiktok.com/', headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0', 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8', 'Accept-Language': 'es-AR,es;q=0.8,en-US;q=0.5,en;q=0.3', 'Connection': 'keep-alive', 'Upgrade-Insecure-Requests': '1', 'Cache-Control': 'max-age=0'})
		return response.cookies.get_dict()['tt_webid']

	def search(self, keyword):
		if self.search_id == False:
			self.search_id = self._search_id()

		cookies = {
			'tt_webid_v2': self.search_id
		}

		headers = {
			'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0',
			'Accept': '*/*',
			'Accept-Language': 'es-AR,es;q=0.8,en-US;q=0.5,en;q=0.3',
			'Referer': 'https://www.tiktok.com/',
			'Connection': 'keep-alive',
			'TE': 'Trailers',
		}

		params = (
			('aid', '1988'),
			('app_language', 'es'),
			('app_name', 'tiktok_web'),
			('browser_language', 'es-AR'),
			('browser_name', 'Mozilla'),
			('browser_online', 'true'),
			('browser_platform', 'Win32'),
			('browser_version', '5.0 (Windows)'),
			('cookie_enabled', 'true'),
			('device_id', self.search_id),
			('device_platform', 'web_pc'),
			('focus_state', 'true'),
			('history_len', '10'),
			('history_list', '%5B%5D'),
			('is_fullscreen', 'false'),
			('is_page_visible', 'true'),
			('keyword', keyword),
			('os', 'windows'),
			('priority_region', ''),
			('referer', ''),
			('region', 'AR'),
			('root_referer', ''),
			('screen_height', '900'),
			('screen_width', '1440'),
			('timezone_name', 'America/Argentina/Mendoza')
		)

		response = requests.get('https://www.tiktok.com/api/search/user/preview/', headers=headers, params=params, cookies=cookies)
		Json = json.loads(response.text)
		results = {}

		for x in Json['sug_list']:
			results[x['extra_info']['unique_id']] = x['extra_info']

		return results


	def trends(self):
		headers = {
			'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0',
			'Accept': 'application/json, text/plain, */*',
			'Accept-Language': 'es-AR,es;q=0.8,en-US;q=0.5,en;q=0.3',
			'Connection': 'keep-alive',
			'Referer': 'https://www.tiktok.com/discover?lang=es',
			'TE': 'Trailers',
		}

		params = (
			('aid', '1988'),
			('app_name', 'tiktok_web'),
			('device_platform', 'web_pc'),
			('region', 'AR'),
			('priority_region', ''),
			('os', 'windows'),
			('referer', 'https://www.google.com/'),
			('root_referer', 'https://www.google.com/'),
			('cookie_enabled', 'true'),
			('screen_width', '1440'),
			('screen_height', '900'),
			('browser_language', 'es-AR'),
			('browser_platform', 'Win32'),
			('browser_name', 'Mozilla'),
			('browser_version', '5.0 (Windows)'),
			('browser_online', 'true'),
			('app_language', 'es'),
			('timezone_name', 'America/Argentina/Mendoza'),
			('is_page_visible', 'true'),
			('focus_state', 'true'),
			('is_fullscreen', 'false'),
			('history_len', '5'),
			('pageType', '6'),
		)

		response = requests.get('https://www.tiktok.com/node/share/discover/list', headers=headers, params=params)
		Json = json.loads(response.text)
		results = {}

		for x in Json['body']['discoverList']:
			results[x['title']] = x

		return results

	def user_info(self, username):
		headers = {
			'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:88.0) Gecko/20100101 Firefox/88.0',
			'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
			'Accept-Language': 'es-AR,es;q=0.8,en-US;q=0.5,en;q=0.3',
			'Connection': 'keep-alive',
			'Upgrade-Insecure-Requests': '1',
		}

		params = (
			('is_copy_url', '1'),
			('is_from_webapp', 'v1'),
		)

		response = requests.get('https://www.tiktok.com/@{}'.format(username), headers=headers, params=params)
		Json = json.loads('{' + response.text.split('crossorigin="anonymous">{')[1].split('</script><script')[0])

		Info_user = {}
		Usuario = Json['props']['pageProps']['userInfo']
		Info_user['Creada_stamp'] = Usuario['user'].get('createTime')
		Info_user['ID'] = Usuario['user'].get('id')
		Info_user['Usuario'] = Usuario['user'].get('uniqueId')
		Info_user['Nombre'] = Usuario['user'].get('nickname')
		Info_user['Descripcion'] = Usuario['user'].get('signature')
		Info_user['Descripcion link'] = Usuario['user'].get('bioLink')
		Info_user['Privada'] = Usuario['user'].get('privateAccount')
		Info_user['Verificada'] = Usuario['user'].get('verified')
		Info_user['Seguidores'] = Usuario['stats'].get('followerCount')
		Info_user['Seguidos'] = Usuario['stats'].get('followingCount')
		Info_user['Videos'] = Usuario['stats'].get('videoCount')
		Info_user['Likes'] = Usuario['stats'].get('heart')

		return Info_user

	def user_videos(self, username):
		headers = {
			'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:88.0) Gecko/20100101 Firefox/88.0',
			'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
			'Accept-Language': 'es-AR,es;q=0.8,en-US;q=0.5,en;q=0.3',
			'Connection': 'keep-alive',
			'Upgrade-Insecure-Requests': '1',
		}

		params = (
			('is_copy_url', '1'),
			('is_from_webapp', 'v1'),
		)

		response = requests.get('https://www.tiktok.com/@{}'.format(username), headers=headers, params=params)
		tt_webid = response.cookies.get_dict()['tt_webid']
		Json_tokens = json.loads('{"props":' + response.text.split('{"props":')[1].split('</script>')[0])
		tt_csrf_token = Json_tokens['props']['initialProps']['$csrfToken']
		Json = json.loads('{' + response.text.split('crossorigin="anonymous">{')[1].split('</script><script')[0])
		
		Videos = {}

		for Video in Json['props']['pageProps']['items']:
			Videos[Video['id']] = Video

		return Videos