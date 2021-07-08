import emoji

message = emoji.emojize('Howdy :sun_with_face:')
message2 = emoji.emojize('Te Amo :red_heart:', variant='emoji_type')

print(f'{message} - {message2}')