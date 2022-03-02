from .api.functions import *
import posixpath
import csv

def attributes():
    """Output file attributes."""
    lexical = [
        'num_dot_url', 'num_hyphen_url', 'num_underline_url',
        'num_bar_url', 'num_question_url', 'num_equal_url',
        'num_atsign_url', 'num_ampersand_url', 'num_exclamation_url',
        'num_space_url', 'num_tilde_url', 'num_comma_url',
        'num_plus_url', 'num_asterisk_url', 'num_hashtag_url',
        'num_dollar_url', 'num_percent_url', 'num_tld_url',
        'length_url', 'num_dot_domain', 'num_hyphen_domain', 'num_underline_domain',
        'num_bar_domain', 'num_question_domain', 'num_equal_domain',
        'num_atsign_domain', 'num_ampersand_domain', 'num_exclamation_domain',
        'num_space_domain', 'num_tilde_domain', 'num_comma_domain',
        'num_plus_domain', 'num_asterisk_domain', 'num_hashtag_domain',
        'num_dollar_domain', 'num_percent_domain', 'length_domain', 'format_ip_domain',
        'server_client_domain', 'num_dot_directory', 'num_hyphen_directory', 'num_underline_directory',
        'num_bar_directory', 'num_question_directory', 'num_equal_directory',
        'num_atsign_directory', 'num_ampersand_directory', 'num_exclamation_directory',
        'num_space_directory', 'num_tilde_directory', 'num_comma_directory',
        'num_plus_directory', 'num_asterisk_directory', 'num_hashtag_directory',
        'num_dollar_directory', 'num_percent_directory', 'length_directory',  'num_dot_file', 'num_hyphen_file', 'num_underline_file',
        'num_bar_file', 'num_question_file', 'num_equal_file',
        'num_atsign_file', 'num_ampersand_file', 'num_exclamation_file',
        'num_space_file', 'num_tilde_file', 'num_comma_file',
        'num_plus_file', 'num_asterisk_file', 'num_hashtag_file',
        'num_dollar_file', 'num_percent_file',
        'length_file', 'num_dot_params', 'num_hyphen_params', 'num_underline_params',
        'num_bar_params', 'num_question_params', 'num_equal_params',
        'num_atsign_params', 'num_ampersand_params', 'num_exclamation_params',
        'num_space_params', 'num_tilde_params', 'num_comma_params',
        'num_plus_params', 'num_asterisk_params', 'num_hashtag_params',
        'num_dollar_params', 'num_percent_params',
        'length_params', 'presence_tld_arguments', 'num_parameters',
        'email_at_url', 'extension_file'
    ]


    host = ['domain_present_in_rbl', 'time_response', 'localtion_geographic_ip',
            'as_number','time_activation_domain', 'time_expiration_domain',
            'num_ip_resolved', 'nameservers', 'num_server_mx', 'value_ttl_associaated']

    others = ['certificate_tls_ssl', 'num_redirect', 'url_index_on_google', 'domain_index_on_google', 'url_shortener']

    list_attributes = []
    list_attributes.extend(lexical)
    list_attributes.extend(host)
    list_attributes.extend(others)
    list_attributes.extend(['phising'])

    return list_attributes

def extract_new_url(url, dataset):
    print(url)
    if (check_Alive(url)):
        with open(dataset, "w", newline='') as output:
            writer = csv.writer(output)
            writer.writerow(attributes())
            dict_url = start_url(url)

            """LEXICAL"""
            # URL
            dot_url = str(count(dict_url['url'], '.'))
            hyphen_url = str(count(dict_url['url'], '-'))
            underline_url = str(count(dict_url['url'], '_'))
            bar_url = str(count(dict_url['url'], '/'))
            question_url = str(count(dict_url['url'], '?'))
            equal_url = str(count(dict_url['url'], '='))
            atsign_url = str(count(dict_url['url'], '@'))
            ampersand_url = str(count(dict_url['url'], '&'))
            exclamation_url = str(count(dict_url['url'], '!'))
            blank_url = str(count(dict_url['url'], ' '))
            til_url = str(count(dict_url['url'], '~'))
            comma_url = str(count(dict_url['url'], ','))
            plus_url = str(count(dict_url['url'], '+'))
            asterisk_url = str(count(dict_url['url'], '*'))
            hashtag_url = str(count(dict_url['url'], '#'))
            money_sign_url = str(count(dict_url['url'], '$'))
            percentage_url = str(count(dict_url['url'], '%'))
            len_url = str(length(dict_url['url']))
            email_exist = str(valid_email(dict_url['url']))
            count_tld_url = str(count_tld(dict_url['url']))
            # DOMAIN
            dot_host = str(count(dict_url['host'], '.'))
            hyphen_host = str(count(dict_url['host'], '-'))
            underline_host = str(count(dict_url['host'], '_'))
            bar_host = str(count(dict_url['host'], '/'))
            question_host = str(count(dict_url['host'], '?'))
            equal_host = str(count(dict_url['host'], '='))
            atsign_host = str(count(dict_url['host'], '@'))
            ampersand_host = str(count(dict_url['host'], '&'))
            exclamation_host = str(count(dict_url['host'], '!'))
            blank_host = str(count(dict_url['host'], ' '))
            til_host = str(count(dict_url['host'], '~'))
            comma_host = str(count(dict_url['host'], ','))
            plus_host = str(count(dict_url['host'], '+'))
            asterisk_host = str(count(dict_url['host'], '*'))
            hashtag_host = str(count(dict_url['host'], '#'))
            money_sign_host = str(count(dict_url['host'], '$'))
            percentage_host = str(count(dict_url['host'], '%'))
            len_host = str(length(dict_url['host']))
            ip_exist = str(valid_ip(dict_url['host']))
            server_client = str(check_word_server_client(dict_url['host']))
            # DIRECTORY
            if dict_url['path']:
                dot_path = str(count(dict_url['path'], '.'))
                hyphen_path = str(count(dict_url['path'], '-'))
                underline_path = str(count(dict_url['path'], '_'))
                bar_path = str(count(dict_url['path'], '/'))
                question_path = str(count(dict_url['path'], '?'))
                equal_path = str(count(dict_url['path'], '='))
                atsign_path = str(count(dict_url['path'], '@'))
                ampersand_path = str(count(dict_url['path'], '&'))
                exclamation_path = str(count(dict_url['path'], '!'))
                blank_path = str(count(dict_url['path'], ' '))
                til_path = str(count(dict_url['path'], '~'))
                comma_path = str(count(dict_url['path'], ','))
                plus_path = str(count(dict_url['path'], '+'))
                asterisk_path = str(count(dict_url['path'], '*'))
                hashtag_path = str(count(dict_url['path'], '#'))
                money_sign_path = str(count(dict_url['path'], '$'))
                percentage_path = str(count(dict_url['path'], '%'))
                len_path = str(length(dict_url['path']))
            else:
                dot_path = -1
                hyphen_path = -1
                underline_path = -1
                bar_path = -1
                question_path = -1
                equal_path = -1
                atsign_path = -1
                ampersand_path = -1
                exclamation_path = -1
                blank_path = -1
                til_path = -1
                comma_path = -1
                plus_path = -1
                asterisk_path = -1
                hashtag_path = -1
                money_sign_path = -1
                percentage_path = -1
                len_path = -1
            # FILE
            if dict_url['path']:
                dot_file = str(count(posixpath.basename(dict_url['path']), '.'))
                hyphen_file = str(count(posixpath.basename(dict_url['path']), '-'))
                underline_file = str(count(posixpath.basename(dict_url['path']), '_'))
                bar_file = str(count(posixpath.basename(dict_url['path']), '/'))
                question_file = str(count(posixpath.basename(dict_url['path']), '?'))
                equal_file = str(count(posixpath.basename(dict_url['path']), '='))
                atsign_file = str(count(posixpath.basename(dict_url['path']), '@'))
                ampersand_file = str(count(posixpath.basename(dict_url['path']), '&'))
                exclamation_file = str(count(posixpath.basename(dict_url['path']), '!'))
                blank_file = str(count(posixpath.basename(dict_url['path']), ' '))
                til_file = str(count(posixpath.basename(dict_url['path']), '~'))
                comma_file = str(count(posixpath.basename(dict_url['path']), ','))
                plus_file = str(count(posixpath.basename(dict_url['path']), '+'))
                asterisk_file = str(count(posixpath.basename(dict_url['path']), '*'))
                hashtag_file = str(count(posixpath.basename(dict_url['path']), '#'))
                money_sign_file = str(count(posixpath.basename(dict_url['path']), '$'))
                percentage_file = str(count(posixpath.basename(dict_url['path']), '%'))
                len_file = str(length(posixpath.basename(dict_url['path'])))
                extension = str(extract_extension(posixpath.basename(dict_url['path'])))
            else:
                dot_file = -1
                hyphen_file = -1
                underline_file = -1
                bar_file = -1
                question_file = -1
                equal_file = -1
                atsign_file = -1
                ampersand_file = -1
                exclamation_file = -1
                blank_file = -1
                til_file = -1
                comma_file = -1
                plus_file = -1
                asterisk_file = -1
                hashtag_file = -1
                money_sign_file = -1
                percentage_file = -1
                len_file = -1
                extension = -1
            # PARAMETERS
            if dict_url['query']:
                dot_params = str(count(dict_url['query'], '.'))
                hyphen_params = str(count(dict_url['query'], '-'))
                underline_params = str(count(dict_url['query'], '_'))
                bar_params = str(count(dict_url['query'], '/'))
                question_params = str(count(dict_url['query'], '?'))
                equal_params = str(count(dict_url['query'], '='))
                atsign_params = str(count(dict_url['query'], '@'))
                ampersand_params = str(count(dict_url['query'], '&'))
                exclamation_params = str(count(dict_url['query'], '!'))
                blank_params = str(count(dict_url['query'], ' '))
                til_params = str(count(dict_url['query'], '~'))
                comma_params = str(count(dict_url['query'], ','))
                plus_params = str(count(dict_url['query'], '+'))
                asterisk_params = str(count(dict_url['query'], '*'))
                hashtag_params = str(count(dict_url['query'], '#'))
                money_sign_params = str(count(dict_url['query'], '$'))
                percentage_params = str(count(dict_url['query'], '%'))
                len_params = str(length(dict_url['query']))
                tld_params = str(check_tld(dict_url['query']))
                number_params = str(count_params(dict_url['query']))
            else:
                dot_params = -1
                hyphen_params = -1
                underline_params = -1
                bar_params = -1
                question_params = -1
                equal_params = -1
                atsign_params = -1
                ampersand_params = -1
                exclamation_params = -1
                blank_params = -1
                til_params = -1
                comma_params = -1
                plus_params = -1
                asterisk_params = -1
                hashtag_params = -1
                money_sign_params = -1
                percentage_params = -1
                len_params = -1
                tld_params = -1
                number_params = -1

            """HOST"""
            rbl = str(check_rbl(dict_url['host']))
            time_domain = str(check_time_response(dict_url['protocol'] + '://' + dict_url['host']))
            asn = str(get_asn_number(dict_url))
            country = str(get_country(dict_url))
            activation_time = str(time_activation_domain(dict_url))
            expiration_time = str(expiration_date_register(dict_url))
            count_ip = str(count_ips(dict_url))
            count_ns = str(count_name_servers(dict_url))
            count_mx = str(count_mx_servers(dict_url))
            ttl = str(extract_ttl(dict_url))

            """OTHERS"""
            ssl = str(check_ssl('https://' + dict_url['url']))
            count_redirect = str(count_redirects(dict_url['protocol'] + '://' + dict_url['url']))
            google_url = str(google_search(dict_url['url']))
            google_domain = str(google_search(dict_url['host']))
            shortener = str(check_shortener(dict_url))

            _lexical = [
                dot_url, hyphen_url, underline_url, bar_url, question_url,
                equal_url, atsign_url, ampersand_url, exclamation_url,
                blank_url, til_url, comma_url, plus_url, asterisk_url, hashtag_url,
                money_sign_url, percentage_url, count_tld_url, len_url, dot_host,
                hyphen_host, underline_host, bar_host, question_host, equal_host,
                atsign_host, ampersand_host, exclamation_host, blank_host, til_host,
                comma_host, plus_host, asterisk_host, hashtag_host, money_sign_host,
                percentage_host, len_host, ip_exist, server_client,
                dot_path, hyphen_path, underline_path, bar_path, question_path,
                equal_path, atsign_path, ampersand_path, exclamation_path,
                blank_path, til_path, comma_path, plus_path, asterisk_path,
                hashtag_path, money_sign_path, percentage_path, len_path, dot_file,
                hyphen_file, underline_file, bar_file, question_file, equal_file,
                atsign_file, ampersand_file, exclamation_file, blank_file,
                til_file, comma_file, plus_file, asterisk_file, hashtag_file,
                money_sign_file, percentage_file, len_file, dot_params,
                hyphen_params, underline_params, bar_params, question_params,
                equal_params, atsign_params, ampersand_params, exclamation_params,
                blank_params, til_params, comma_params, plus_params, asterisk_params,
                hashtag_params, money_sign_params, percentage_params, len_params,
                tld_params, number_params, email_exist, extension
            ]

            _host = [rbl, time_domain, country, asn, activation_time,
                        expiration_time, count_ip, count_ns, count_mx, ttl]

            _others = [ssl, count_redirect, google_url, google_domain, shortener]
            

            result = []
            result.extend(_lexical)
            result.extend(_host)
            result.extend(_others)
            result.extend([''])
            print(result)
            writer.writerow(result)
    else:
        print('This page is not online')

def generate_dataset(urls, dataset, phising):
    with open(dataset, "w", newline='') as output:
        writer = csv.writer(output)
        writer.writerow(attributes())
        count_url = 0
        for url in read_file(urls):
            if (check_Alive(url)):
                print(url)
                count_url = count_url + 1
                dict_url = start_url(url)

                """LEXICAL"""
                # URL
                dot_url = str(count(dict_url['url'], '.'))
                hyphen_url = str(count(dict_url['url'], '-'))
                underline_url = str(count(dict_url['url'], '_'))
                bar_url = str(count(dict_url['url'], '/'))
                question_url = str(count(dict_url['url'], '?'))
                equal_url = str(count(dict_url['url'], '='))
                atsign_url = str(count(dict_url['url'], '@'))
                ampersand_url = str(count(dict_url['url'], '&'))
                exclamation_url = str(count(dict_url['url'], '!'))
                blank_url = str(count(dict_url['url'], ' '))
                til_url = str(count(dict_url['url'], '~'))
                comma_url = str(count(dict_url['url'], ','))
                plus_url = str(count(dict_url['url'], '+'))
                asterisk_url = str(count(dict_url['url'], '*'))
                hashtag_url = str(count(dict_url['url'], '#'))
                money_sign_url = str(count(dict_url['url'], '$'))
                percentage_url = str(count(dict_url['url'], '%'))
                len_url = str(length(dict_url['url']))
                email_exist = str(valid_email(dict_url['url']))
                count_tld_url = str(count_tld(dict_url['url']))
                # DOMAIN
                dot_host = str(count(dict_url['host'], '.'))
                hyphen_host = str(count(dict_url['host'], '-'))
                underline_host = str(count(dict_url['host'], '_'))
                bar_host = str(count(dict_url['host'], '/'))
                question_host = str(count(dict_url['host'], '?'))
                equal_host = str(count(dict_url['host'], '='))
                atsign_host = str(count(dict_url['host'], '@'))
                ampersand_host = str(count(dict_url['host'], '&'))
                exclamation_host = str(count(dict_url['host'], '!'))
                blank_host = str(count(dict_url['host'], ' '))
                til_host = str(count(dict_url['host'], '~'))
                comma_host = str(count(dict_url['host'], ','))
                plus_host = str(count(dict_url['host'], '+'))
                asterisk_host = str(count(dict_url['host'], '*'))
                hashtag_host = str(count(dict_url['host'], '#'))
                money_sign_host = str(count(dict_url['host'], '$'))
                percentage_host = str(count(dict_url['host'], '%'))
                len_host = str(length(dict_url['host']))
                ip_exist = str(valid_ip(dict_url['host']))
                server_client = str(check_word_server_client(dict_url['host']))
                # DIRECTORY
                if dict_url['path']:
                    dot_path = str(count(dict_url['path'], '.'))
                    hyphen_path = str(count(dict_url['path'], '-'))
                    underline_path = str(count(dict_url['path'], '_'))
                    bar_path = str(count(dict_url['path'], '/'))
                    question_path = str(count(dict_url['path'], '?'))
                    equal_path = str(count(dict_url['path'], '='))
                    atsign_path = str(count(dict_url['path'], '@'))
                    ampersand_path = str(count(dict_url['path'], '&'))
                    exclamation_path = str(count(dict_url['path'], '!'))
                    blank_path = str(count(dict_url['path'], ' '))
                    til_path = str(count(dict_url['path'], '~'))
                    comma_path = str(count(dict_url['path'], ','))
                    plus_path = str(count(dict_url['path'], '+'))
                    asterisk_path = str(count(dict_url['path'], '*'))
                    hashtag_path = str(count(dict_url['path'], '#'))
                    money_sign_path = str(count(dict_url['path'], '$'))
                    percentage_path = str(count(dict_url['path'], '%'))
                    len_path = str(length(dict_url['path']))
                else:
                    dot_path = -1
                    hyphen_path = -1
                    underline_path = -1
                    bar_path = -1
                    question_path = -1
                    equal_path = -1
                    atsign_path = -1
                    ampersand_path = -1
                    exclamation_path = -1
                    blank_path = -1
                    til_path = -1
                    comma_path = -1
                    plus_path = -1
                    asterisk_path = -1
                    hashtag_path = -1
                    money_sign_path = -1
                    percentage_path = -1
                    len_path = -1
                # FILE
                if dict_url['path']:
                    dot_file = str(count(posixpath.basename(dict_url['path']), '.'))
                    hyphen_file = str(count(posixpath.basename(dict_url['path']), '-'))
                    underline_file = str(
                        count(posixpath.basename(dict_url['path']), '_'))
                    bar_file = str(count(posixpath.basename(dict_url['path']), '/'))
                    question_file = str(
                        count(posixpath.basename(dict_url['path']), '?'))
                    equal_file = str(count(posixpath.basename(dict_url['path']), '='))
                    atsign_file = str(count(posixpath.basename(dict_url['path']), '@'))
                    ampersand_file = str(
                        count(posixpath.basename(dict_url['path']), '&'))
                    exclamation_file = str(
                        count(posixpath.basename(dict_url['path']), '!'))
                    blank_file = str(count(posixpath.basename(dict_url['path']), ' '))
                    til_file = str(count(posixpath.basename(dict_url['path']), '~'))
                    comma_file = str(count(posixpath.basename(dict_url['path']), ','))
                    plus_file = str(count(posixpath.basename(dict_url['path']), '+'))
                    asterisk_file = str(
                        count(posixpath.basename(dict_url['path']), '*'))
                    hashtag_file = str(
                        count(posixpath.basename(dict_url['path']), '#'))
                    money_sign_file = str(
                        count(posixpath.basename(dict_url['path']), '$'))
                    percentage_file = str(
                        count(posixpath.basename(dict_url['path']), '%'))
                    len_file = str(length(posixpath.basename(dict_url['path'])))
                    extension = str(extract_extension(
                        posixpath.basename(dict_url['path'])))
                else:
                    dot_file = -1
                    hyphen_file = -1
                    underline_file = -1
                    bar_file = -1
                    question_file = -1
                    equal_file = -1
                    atsign_file = -1
                    ampersand_file = -1
                    exclamation_file = -1
                    blank_file = -1
                    til_file = -1
                    comma_file = -1
                    plus_file = -1
                    asterisk_file = -1
                    hashtag_file = -1
                    money_sign_file = -1
                    percentage_file = -1
                    len_file = -1
                    extension = -1
                # PARAMETERS
                if dict_url['query']:
                    dot_params = str(count(dict_url['query'], '.'))
                    hyphen_params = str(count(dict_url['query'], '-'))
                    underline_params = str(count(dict_url['query'], '_'))
                    bar_params = str(count(dict_url['query'], '/'))
                    question_params = str(count(dict_url['query'], '?'))
                    equal_params = str(count(dict_url['query'], '='))
                    atsign_params = str(count(dict_url['query'], '@'))
                    ampersand_params = str(count(dict_url['query'], '&'))
                    exclamation_params = str(count(dict_url['query'], '!'))
                    blank_params = str(count(dict_url['query'], ' '))
                    til_params = str(count(dict_url['query'], '~'))
                    comma_params = str(count(dict_url['query'], ','))
                    plus_params = str(count(dict_url['query'], '+'))
                    asterisk_params = str(count(dict_url['query'], '*'))
                    hashtag_params = str(count(dict_url['query'], '#'))
                    money_sign_params = str(count(dict_url['query'], '$'))
                    percentage_params = str(count(dict_url['query'], '%'))
                    len_params = str(length(dict_url['query']))
                    tld_params = str(check_tld(dict_url['query']))
                    number_params = str(count_params(dict_url['query']))
                else:
                    dot_params = -1
                    hyphen_params = -1
                    underline_params = -1
                    bar_params = -1
                    question_params = -1
                    equal_params = -1
                    atsign_params = -1
                    ampersand_params = -1
                    exclamation_params = -1
                    blank_params = -1
                    til_params = -1
                    comma_params = -1
                    plus_params = -1
                    asterisk_params = -1
                    hashtag_params = -1
                    money_sign_params = -1
                    percentage_params = -1
                    len_params = -1
                    tld_params = -1
                    number_params = -1

                """HOST"""
                rbl = str(check_rbl(dict_url['host']))
                time_domain = str(check_time_response(dict_url['protocol'] + '://' + dict_url['host']))
                asn = str(get_asn_number(dict_url))
                country = str(get_country(dict_url))
                activation_time = str(time_activation_domain(dict_url))
                expiration_time = str(expiration_date_register(dict_url))
                count_ip = str(count_ips(dict_url))
                count_ns = str(count_name_servers(dict_url))
                count_mx = str(count_mx_servers(dict_url))
                ttl = str(extract_ttl(dict_url))

                """OTHERS"""
                ssl = str(check_ssl('https://' + dict_url['url']))
                count_redirect = str(count_redirects(
                    dict_url['protocol'] + '://' + dict_url['url']))
                google_url = str(google_search(dict_url['url']))
                google_domain = str(google_search(dict_url['host']))
                shortener = str(check_shortener(dict_url))

                _lexical = [
                    dot_url, hyphen_url, underline_url, bar_url, question_url,
                    equal_url, atsign_url, ampersand_url, exclamation_url,
                    blank_url, til_url, comma_url, plus_url, asterisk_url, hashtag_url,
                    money_sign_url, percentage_url, count_tld_url, len_url, dot_host,
                    hyphen_host, underline_host, bar_host, question_host, equal_host,
                    atsign_host, ampersand_host, exclamation_host, blank_host, til_host,
                    comma_host, plus_host, asterisk_host, hashtag_host, money_sign_host,
                    percentage_host, len_host, ip_exist, server_client,
                    dot_path, hyphen_path, underline_path, bar_path, question_path,
                    equal_path, atsign_path, ampersand_path, exclamation_path,
                    blank_path, til_path, comma_path, plus_path, asterisk_path,
                    hashtag_path, money_sign_path, percentage_path, len_path, dot_file,
                    hyphen_file, underline_file, bar_file, question_file, equal_file,
                    atsign_file, ampersand_file, exclamation_file, blank_file,
                    til_file, comma_file, plus_file, asterisk_file, hashtag_file,
                    money_sign_file, percentage_file, len_file, dot_params,
                    hyphen_params, underline_params, bar_params, question_params,
                    equal_params, atsign_params, ampersand_params, exclamation_params,
                    blank_params, til_params, comma_params, plus_params, asterisk_params,
                    hashtag_params, money_sign_params, percentage_params, len_params,
                    tld_params, number_params, email_exist, extension
                ]


                _host = [rbl, time_domain, country, asn, activation_time,
                            expiration_time, count_ip, count_ns, count_mx, ttl]

                _others = [ssl, count_redirect, google_url, google_domain, shortener]

                result = []
                result.extend(_lexical)
                result.extend(_host)
                result.extend(_others)
                result.extend([phising])
                print(count_url)
                print(result)
                writer.writerow(result)
            else:
                print("failed")