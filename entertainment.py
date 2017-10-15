import fresh_tomatoes
import media

judwaa_2 = media.Movie('Judwaa 2',
                     'Raja and Prem - the iconic Jodi from Judwaa 2 are back after 20 years. Superstar Varun Dhawan, who is known for his comic timing, is set to entertain audiences through this rib-tickling comedy that promises to be an all-out family entertainer. Setting the temperatures soaring are two of the hottest actresses - Jacqueline Fernandes and Taapsee Pannu, in a never-seen-before avatar. The plotline of the film being directed by the master of comedies, David Dhawan, promises Double The Fun, Double The Entertainment. The laugh riot is set in Mumbai and in London and the twins create confusion in both these worlds only to save the day in the end. Presented by Fox Star Studios, Judwaa 2 is produced by Sajid Nadiadwala and is set to release on September 29.',
                    'https://upload.wikimedia.org/wikipedia/en/9/91/Judwaa_2_Poster.jpg',
                     'https://www.youtube.com/watch?v=DDwbjWCgxVM')

victoria_abdul = media.Movie('Victoria Abdul',
                           'The extraordinary true story of an unexpected friendship in the later years of Queen Victorias (Academy Award winner Judi Dench) remarkable rule. When Abdul Karim (Ali Fazal), a young clerk, travels from India to participate in the Queens Golden Jubilee, he is surprised to find favor with the Queen herself. As the Queen questions the constrictions of her long-held position, the two forge an unlikely and devoted alliance with a loyalty to one another that her household and inner circle all attempt to destroy. As the friendship deepens, the Queen begins to see a changing world through new eyes and joyfully reclaims her humanity.',
                           'https://upload.wikimedia.org/wikipedia/en/3/36/VictoriaAndAbdulPoster.jpg',
                            'https://www.youtube.com/watch?v=BT2Ph_9bGPs')
newton = media.Movie('Newton',
                   'A government clerk on election duty in the conflict ridden jungle of Central India tries his best to conduct free and fair voting despite the apathy of security forces and the looming fear of guerrilla attacks by communist rebels.',
                      'https://upload.wikimedia.org/wikipedia/en/6/68/Newton_%28film%29.png',
                     'https://www.youtube.com/watch?v=yU6zMPFd4UU')

chef = media.Movie('Chef',
                     'Chef Roshan Kalra sets out to find the true source of happiness and reignite his passion for food while being more present in his sons life.',
                   'https://upload.wikimedia.org/wikipedia/en/0/01/Chef_-_Poster.jpg',
                   'https://www.youtube.com/watch?v=YaFJXd3ciLs')
the_accountant = media.Movie('The Accountant',
                               'Accountant Christian Wolff works for various illegal companies and manipulates their financial records. When the FBI learns about his truth, he takes up a legitimate client to bluff the officers.',
                                'https://upload.wikimedia.org/wikipedia/en/e/e4/The_Accountant_%282016_film%29.png',
                                'https://www.youtube.com/watch?v=DBfsgcswlYQ')
the_jungle_book = media.Movie('The jungle book',
                                 'After a threat from the tiger Shere Khan forces him to flee the jungle, a man-cub named Mowgli embarks on a journey of self discovery with the help of panther, Bagheera, and free spirited bear, Baloo.',
                              'https://upload.wikimedia.org/wikipedia/en/a/a4/The_Jungle_Book_%282016%29.jpg',
                              'https://www.youtube.com/watch?v=C4qgAaxB_pc')

movies = [judwaa_2, victoria_abdul, newton, chef, the_accountant, the_jungle_book]
fresh_tomatoes.open_movies_page(movies)





