import sys
import re
from urllib import request
from urllib.error import URLError


ALLOWED_ERROR_CODES = [200, 403]
ALLOWED_TRANSPORT_TYPES = ['HTTP', 'HTTPS']


#
# Emma Note 1:
# Ideally this function would be run on a distributed
# multiprocessing environment, such as a task queue or
# event system. This would enable the job to be scaled
# infinitely as needed.
#
def check_links(urls):
	if type(urls) is str:
		urls = [urls]
	elif type(urls) not in [list, tuple]:
		raise ValueError("Input must be of type list or tuple")

	#
	# Emma Note 2:
	# Links could be cached in a key-value store with a
	# small TTL to skip checking of repetitive links. This
	# will speed up checks considerably assuming high load.
	#
	result = []
	for url in urls:
		#
		# Emma Note 3:
		# As URLs are very permissive with syntax, the only
		# good check to do is make sure we're doing HTTP/S,
		# alternatively use ALLOWED_TRANSPORT_TYPES from
		# above to allow certain protocols. urllib will take
		# care of validating the URL before submitting an
		# actual request.
		#
		if not url.startswith("http://") and not url.startswith("https://"):
			result.append((url, "Link must be HTTP/HTTPS hyperlink"))
			continue

		try:
			req = request.Request(url)
			ret	= request.urlopen(req)
		except ValueError as exc:
			result.append((url, "Link is not well formed"))
		except URLError as exc:
			result.append((url, exc.reason))
		else:
			if ret.status not in ALLOWED_ERROR_CODES:
				result.append((url, "Link returned status code: %d" % ret.status))
	#
	# Emma Note 4:
	# Ideally results would be stored in a shared storage back-
	# end, so that any front-end interface that dispatches a job
	# can see real-time status whether the job is completed or
	# not.
	#
	return result


def main():
	args = sys.argv[1:]

	print("URL\t\t\tResult")
	for result in check_links(args):
		print("%s\t\t\t%s" % result)


if __name__ == "__main__":
	main()
