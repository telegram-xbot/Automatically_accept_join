const TOKEN = process.env.BOT_TOKEN;

async function telegram(method, data) {
  return fetch(`https://api.telegram.org/bot${TOKEN}/${method}`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json"
    },
    body: JSON.stringify(data)
  });
}

module.exports = async (req, res) => {

  const update = req.body;

  // Auto Approve Join Request
  if (update.chat_join_request) {

    const chatId = update.chat_join_request.chat.id;
    const userId = update.chat_join_request.from.id;

    await telegram("approveChatJoinRequest", {
      chat_id: chatId,
      user_id: userId
    });

    await telegram("sendMessage", {
      chat_id: userId,
      text: "🎉 Your join request has been approved!\n\nWelcome ❤️",
      reply_markup: {
        inline_keyboard: [
          [
            {
              text: "📢 Channel 1",
              url: "https://t.me/vedioss_pro"
            }
          ],
          [
            {
              text: "📢 Channel 2",
              url: "https://t.me/premium_collection_vedio"
            }
          ],
          [
            {
              text: "📢 Channel 3",
              url: "https://t.me/More_vedios_bot"
            }
          ],
          [
            {
              text: "📢 Channel 4",
              url: "https://t.me/Baap_robot"
            }
          ],
          [
            {
              text: "➕ Add In Your Channel",
              url: "https://t.me/Automatically_join_accept_bot?startchannel"
            }
          ]
        ]
      }
    });
  }

  // Start Command
  if (update.message && update.message.text === "/start") {

    await telegram("sendMessage", {
      chat_id: update.message.chat.id,
      text: "🤖 Auto Join Accept Bot",
      reply_markup: {
        inline_keyboard: [
          [
            {
              text: "📢 Add Me To Channel",
              url: "https://t.me/Automatically_join_accept_bot?startchannel"
            }
          ],
          [
            {
              text: "👥 Add Me To Group",
              url: "https://t.me/Automatically_join_accept_bot?startgroup=true"
            }
          ],
          [
            {
              text: "👨‍💻 Support Channel",
              url: "https://t.me/vedioss_pro"
            }
          ]
        ]
      }
    });
  }

  res.status(200).json({ ok: true });
};
