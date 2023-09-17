"""
Пожалуйста, приступайте к этой задаче после того, как вы сделали и получили ревью ко всем остальным задачам
в этом репозитории. Она значительно сложнее.


Есть набор сообщений из чата в следующем формате:

```
messages = [
    {
        "id": "efadb781-9b04-4aad-9afe-e79faef8cffb",
        "sent_at": datetime.datetime(2022, 10, 11, 23, 11, 11, 721),
        "sent_by": 46,  # id пользователя-отправителя
        "reply_for": "7b22ae19-6c58-443e-b138-e22784878581",  # id сообщение, на которое это сообщение является ответом (может быть None)
        "seen_by": [26, 91, 71], # идентификаторы пользователей, которые видели это сообщение
        "text": "А когда ревью будет?",
    }
]
```

Так же есть функция `generate_chat_history`, которая вернёт список из большого количества таких сообщений.
Установите библиотеку lorem, чтобы она работала.

Нужно:
1. Вывести айди пользователя, который написал больше всех сообщений.
2. Вывести айди пользователя, на сообщения которого больше всего отвечали.
3. Вывести айди пользователей, сообщения которых видело больше всего уникальных пользователей.
4. Определить, когда в чате больше всего сообщений: утром (до 12 часов), днём (12-18 часов) или вечером (после 18 часов).
5. Вывести идентификаторы сообщений, который стали началом для самых длинных тредов (цепочек ответов).

Весь код стоит разбить на логические части с помощью функций.
"""
import random
import uuid
import datetime

import lorem


def generate_chat_history():
    messages_amount = random.randint(200, 1000)
    users_ids = list(
        {random.randint(1, 10000) for _ in range(random.randint(5, 20))}
    )
    sent_at = datetime.datetime.now() - datetime.timedelta(days=100)
    messages = []
    for _ in range(messages_amount):
        sent_at += datetime.timedelta(minutes=random.randint(0, 240))
        messages.append({
            "id": uuid.uuid4(),
            "sent_at": sent_at,
            "sent_by": random.choice(users_ids),
            "reply_for": random.choice(
                [
                    None,
                    (
                        random.choice([m["id"] for m in messages])
                        if messages else None
                    ),
                ],
            ),
            "seen_by": random.sample(users_ids,
                                     random.randint(1, len(users_ids))),
            "text": lorem.sentence(),
        })
    return messages


if __name__ == "__main__":
    messages = (generate_chat_history())
    # print(messages)


def most_write_messages():
    author_messages = {}
    for message in messages:
        author_messages[message['sent_by']] = author_messages.get(message['sent_by'], 0) + 1
    max_messages = max(author_messages.values())
    for k, v in author_messages.items():
        if v == max_messages:
            return k


print(f'Больше всего сообщений написал пользователь с номером {most_write_messages()}')


def most_reply():
    author_messages = {}
    for message in messages:
        for reply in messages:
            if message['id'] == reply['reply_for']:
                author_messages[message['sent_by']] = author_messages.get(message['sent_by'], 0) + 1
    max_messages = max(author_messages.values())
    for k, v in author_messages.items():
        if v == max_messages:
            return k


print(f'Больше всего ответов на сообщения, которые написал пользователь с номером {most_reply()}')


def most_seen():
    author_messages = {}
    for message in messages:
        if message['sent_by'] not in author_messages:
            author_messages[message['sent_by']] = message['seen_by']
        else:
            for user_id in message['seen_by']:
                if user_id not in author_messages[message['sent_by']]:
                    author_messages[message['sent_by']].append(user_id)
    max_user = 0
    for user_list in author_messages.values():
        if len(user_list) > max_user:
            max_user = len(user_list)
    max_list = []
    for k, v in author_messages.items():
        if len(v) == max_user:
            max_list.append(k)
    if len(max_list) > 1:
        return max_list
    return k


print(f'Сообщения, которые видели больше всего уникальных пользователей, написал пользователь с номером {most_seen()}')


def time_max():
    message_time = {'Утром': 0, 'Днём': 0, 'Вечером': 0}
    for message in messages:
        if message['sent_at'].hour < 12:
            message_time['Утром'] += 1
        elif 12 < message['sent_at'].hour < 18:
            message_time['Днём'] += 1
        else:
            message_time['Вечером'] += 1
    max_time = max(message_time.values())
    for k, v in message_time.items():
        if v == max_time:
            return k


print(f'Больше всего сообщений было {time_max()}')


def find_longest_threads():
    thread_lengths = {}

    for message in messages:
        thread_length = 0
        current_message = message
        while current_message is not None:
            thread_length += 1
            current_message = next((m for m in messages if m['id'] == current_message['reply_for']), None)
        thread_lengths[message['id']] = thread_length

    max_length = max(thread_lengths.values())
    longest_threads = []
    for k,v in thread_lengths.items():
        if v == max_length:
            longest_threads.append(k)
    return longest_threads


print(f'Самая длинная цепочка ответов у сообщений с id: {find_longest_threads()}')