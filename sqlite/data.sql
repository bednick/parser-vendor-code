INSERT INTO templates (template_id, name, mask, value)
VALUES
    ('00000000-0000-0000-0000-template0001', 'Поршневые серии С', 'C Х/ХхХ-Х.Х.ХХ(Х)(Х)', '(?P<series>C)\s*\s+\s*(?P<D>\d+)\s*\/\s*(?P<d>\d+)\s*[xX\*]\s*(?P<S>\d+)\s*-\s*(?P<pressure>\d+)\s*.\s*(?P<attachment>\d+)\s*.?\s*(?P<working_fluid>\d+)?\s*.?\s*(?P<hydraulic_cylinder>A|K|C|F|D|РТ)?\s*(?P<climatic>T|YXL|XL)?\s*\(\s*(?P<L>\d+)\s*\)\s*\(?\s*(?P<supply_hydraulic_cylinders>\d+)?\s*\)?')
    , ('00000000-0000-0000-0000-template0002', 'Поршневые серии МС', 'МC Х/ХхХ-Х.Х.Х.ХХ(Х)(Х)', '(?P<series>MC)\s*\s+\s*(?P<D>\d+)\s*\/\s*(?P<d>\d+)\s*[xX\*]\s*(?P<S>\d+)\s*-\s*(?P<pressure>\d+)\s*.\s*(?P<attachment>\d+)\s*.?\s*(?P<working_fluid>\d+)?\s*.?\s*(?P<hydraulic_cylinder>A|K|C|F|D|РТ)?\s*(?P<climatic>T|YXL|XL)?\s*\(\s*(?P<L>\d+)\s*\)\s*\(?\s*(?P<supply_hydraulic_cylinders>\d+)?\s*\)?')
    , ('00000000-0000-0000-0000-template0003', 'Плунжерные серии МСP', 'МСР ХхХ-Х.Х.Х.ХХ(Х)(Х)', '(?P<series>MCP)\s*\s+\s*(?P<d>\d+)\s*[xX\*]\s*(?P<S>\d+)\s*-\s*(?P<pressure>\d+)\s*.\s*(?P<attachment>\d+)\s*.?\s*(?P<working_fluid>\d+)?\s*.?\s*(?P<hydraulic_cylinder>A|K|C|F|D|РТ)?\s*(?P<climatic>T|YXL|XL)?\s*\(\s*(?P<L>\d+)\s*\)\s*\(?\s*(?P<supply_hydraulic_cylinders>\d+)?\s*\)?')
;

INSERT INTO directories (directory_id, name)
VALUES
    ('00000000-0000-0000-0000-directory002', 'Исполнение по номинальному давлению')
    , ('00000000-0000-0000-0000-directory003', 'Исполнение по способу крепления гидроцилиндров')
    , ('00000000-0000-0000-0000-directory004', 'Исполнение по подводу рабочей жидкости')
    , ('00000000-0000-0000-0000-directory005', 'Конструктивное исполнение гидроцилиндра')
    , ('00000000-0000-0000-0000-directory006', 'Климатическое исполнение')
;

INSERT INTO directory_values (directory_id, key, value)
VALUES
    ('00000000-0000-0000-0000-directory002', '3', '16 МПа')
    , ('00000000-0000-0000-0000-directory002', '4', '20 МПа')
    , ('00000000-0000-0000-0000-directory002', '5', '25 МПа')
    , ('00000000-0000-0000-0000-directory002', '6', '28 МПа')

    , ('00000000-0000-0000-0000-directory003', '00', 'Корпус и шток с подготовленными концами под сварку')
    , ('00000000-0000-0000-0000-directory003', '01', 'Корпус с подготовкой конца под сварку и проушина с шарнирным подшипником на штоке')
    , ('00000000-0000-0000-0000-directory003', '02', 'Корпус с подготовкой конца под сварку и шток с проушиной')
    , ('00000000-0000-0000-0000-directory003', '04', 'Корпус с подготовкой конца под сварку и шток с вилкой')
    , ('00000000-0000-0000-0000-directory003', '05', 'Корпус с подготовкой конца под сварку и шток с резьбой')
    , ('00000000-0000-0000-0000-directory003', '07', 'Корпус с подготовкой конца под сварку и шток с разъемной головкой')
    , ('00000000-0000-0000-0000-directory003', '08', 'Корпус с подготовкой конца под сварку и шток со сферой или грибком')
    , ('00000000-0000-0000-0000-directory003', '09', 'Корпус с подготовкой конца под сварку и шток с фланцем')
    , ('00000000-0000-0000-0000-directory003', '10', 'Проушина с шарнирным подшипником на корпусе и шток с подготовкой конца под сварку')
    , ('00000000-0000-0000-0000-directory003', '11', 'Проушины с шарнирным подшипником на корпусе и штоке')
    , ('00000000-0000-0000-0000-directory003', '12', 'Проушина с шарнирным подшипником на корпусе и шток с проушиной')
    , ('00000000-0000-0000-0000-directory003', '14', 'Проушина с шарнирным подшипником на корпусе и шток с вилкой')
    , ('00000000-0000-0000-0000-directory003', '15', 'Проушина с шарнирным подшипником на корпусе и шток с резьбой')
    , ('00000000-0000-0000-0000-directory003', '17', 'Проушина с шарнирным подшипником на корпусе и шток с разъемной головкой')
    , ('00000000-0000-0000-0000-directory003', '18', 'Проушина с шарнирным подшипником на корпусе и шток со сферой или грибком')
    , ('00000000-0000-0000-0000-directory003', '19', 'Проушина с шарнирным подшипником на корпусе и шток с фланцем')
    , ('00000000-0000-0000-0000-directory003', '20', 'Проушина на корпусе и шток с подготовкой конца под сварку')
    , ('00000000-0000-0000-0000-directory003', '21', 'Проушина на корпусе и шарнирный подшипник на штоке')
    , ('00000000-0000-0000-0000-directory003', '22', 'Проушины на корпусе и штоке')
    , ('00000000-0000-0000-0000-directory003', '24', 'Проушина на корпусе и шток с вилкой')
    , ('00000000-0000-0000-0000-directory003', '25', 'Проушина на корпусе и шток с резьбой')
    , ('00000000-0000-0000-0000-directory003', '27', 'Проушина на корпусе и шток с разъемной головкой')
    , ('00000000-0000-0000-0000-directory003', '28', 'Проушина на корпусе и шток со сферой или грибком')
    , ('00000000-0000-0000-0000-directory003', '29', 'Проушина на корпусе и шток с фланцем')
    , ('00000000-0000-0000-0000-directory003', '30', 'Корпус на цапфах и шток с подготовкой конца под сварку')
    , ('00000000-0000-0000-0000-directory003', '31', 'Корпус на цапфах и проушина с шарнирным подшипником на штоке')
    , ('00000000-0000-0000-0000-directory003', '32', 'Корпус на цапфах и проушина на штоке')
    , ('00000000-0000-0000-0000-directory003', '34', 'Корпус на цапфах и шток с вилкой')
    , ('00000000-0000-0000-0000-directory003', '35', 'Корпус на цапфах и шток с резьбой')
    , ('00000000-0000-0000-0000-directory003', '37', 'Корпус на цапфах и шток с разъемной головкой')
    , ('00000000-0000-0000-0000-directory003', '38', 'Корпус на цапфах и шток со сферой или грибком')
    , ('00000000-0000-0000-0000-directory003', '39', 'Корпус на цапфах и шток с фланцем')
    , ('00000000-0000-0000-0000-directory003', '40', 'Вилка на корпусе и шток с подготовкой конца под сварку')
    , ('00000000-0000-0000-0000-directory003', '41', 'Вилка на корпусе и проушина с шарнирным подшипником на штоке')
    , ('00000000-0000-0000-0000-directory003', '42', 'Вилка на корпусе и проушина на штоке')
    , ('00000000-0000-0000-0000-directory003', '44', 'Вилка на корпусе и штоке')
    , ('00000000-0000-0000-0000-directory003', '45', 'Вилка на корпусе и шток с резьбой')
    , ('00000000-0000-0000-0000-directory003', '47', 'Вилка на корпусе и шток с разъемной головкой')
    , ('00000000-0000-0000-0000-directory003', '48', 'Вилка на корпусе и шток со сферой или грибком')
    , ('00000000-0000-0000-0000-directory003', '49', 'Вилка на корпусе и шток с фланцем')
    , ('00000000-0000-0000-0000-directory003', '50', 'Корпус с резьбой и шток с подготовкой конца под сварку')
    , ('00000000-0000-0000-0000-directory003', '51', 'Корпус с резьбой и проушина с шарнирным подшипником на штоке')
    , ('00000000-0000-0000-0000-directory003', '52', 'Корпус с резьбой и проушина на штоке')
    , ('00000000-0000-0000-0000-directory003', '54', 'Корпус с резьбой и шток с вилкой')
    , ('00000000-0000-0000-0000-directory003', '55', 'Корпус с резьбой и шток с резьбой')
    , ('00000000-0000-0000-0000-directory003', '57', 'Корпус с резьбой и шток с разъемной головкой')
    , ('00000000-0000-0000-0000-directory003', '58', 'Корпус с резьбой и шток со сферой или грибком')
    , ('00000000-0000-0000-0000-directory003', '59', 'Корпус с резьбой и шток с фланцем')
    , ('00000000-0000-0000-0000-directory003', '70', 'Корпус с разъемной проушиной и шток с подготовкой конца под сварку')
    , ('00000000-0000-0000-0000-directory003', '71', 'Корпус с разъемной проушиной и проушина с шарнирным подшипником на штоке')
    , ('00000000-0000-0000-0000-directory003', '72', 'Корпус с разъемной проушиной и проушина на штоке')
    , ('00000000-0000-0000-0000-directory003', '74', 'Корпус с разъемной проушиной и шток с вилкой')
    , ('00000000-0000-0000-0000-directory003', '75', 'Корпус с разъемной проушиной и шток с резьбой')
    , ('00000000-0000-0000-0000-directory003', '77', 'Корпус с разъемной проушиной и шток с разъемной проушиной')
    , ('00000000-0000-0000-0000-directory003', '78', 'Корпус с разъемной проушиной и шток со сферой или грибком')
    , ('00000000-0000-0000-0000-directory003', '79', 'Корпус с разъемной проушиной и шток с фланцем')
    , ('00000000-0000-0000-0000-directory003', '80', 'Корпус со сферой или грибком и шток с подготовкой конца под сварку')
    , ('00000000-0000-0000-0000-directory003', '81', 'Корпус со сферой или грибком и проушина с шарнирным подшипником на штоке')
    , ('00000000-0000-0000-0000-directory003', '82', 'Корпус со сферой или грибком и проушина на штоке')
    , ('00000000-0000-0000-0000-directory003', '84', 'Корпус со сферой или грибком и шток с вилкой')
    , ('00000000-0000-0000-0000-directory003', '85', 'Корпус со сферой или грибком и шток с резьбой')
    , ('00000000-0000-0000-0000-directory003', '87', 'Корпус со сферой или грибком и шток с разъемной проушиной')
    , ('00000000-0000-0000-0000-directory003', '88', 'Корпус со сферой или грибком и шток со сферой или грибком')
    , ('00000000-0000-0000-0000-directory003', '89', 'Корпус со сферой или грибком и шток с фланцем')
    , ('00000000-0000-0000-0000-directory003', '90', 'Корпус с фланцем и шток с подготовкой конца под сварку')
    , ('00000000-0000-0000-0000-directory003', '91', 'Корпус с фланцем и проушина с шарнирным подшипником на штоке')
    , ('00000000-0000-0000-0000-directory003', '92', 'Корпус с фланцем и проушина на штоке')
    , ('00000000-0000-0000-0000-directory003', '94', 'Корпус с фланцем и шток с вилкой')
    , ('00000000-0000-0000-0000-directory003', '95', 'Корпус с фланцем и шток с резьбой')
    , ('00000000-0000-0000-0000-directory003', '97', 'Корпус с фланцем и шток с разъемной проушиной')
    , ('00000000-0000-0000-0000-directory003', '98', 'Корпус с фланцем и шток со сферой или грибком')
    , ('00000000-0000-0000-0000-directory003', '99', 'Корпус с фланцем и шток с фланцем')

    , ('00000000-0000-0000-0000-directory004', '0', 'Бонка с внутренней резьбой')
    , ('00000000-0000-0000-0000-directory004', '1', 'Бонки с внутренней резьбой расположены в зоне передней крышки с подводом маслопровода')
    , ('00000000-0000-0000-0000-directory004', '2', 'Бонка с угловым штуцером с наружной резьбой')
    , ('00000000-0000-0000-0000-directory004', '3', 'Штуцер с наружной резьбой')
    , ('00000000-0000-0000-0000-directory004', '4', 'Бонки с внутренней резьбой, расположенные под углом друг к другу')
    , ('00000000-0000-0000-0000-directory004', '5', 'Штуцеры с наружной резьбой, расположенные под углом друг к другу')
    , ('00000000-0000-0000-0000-directory004', '6', 'Фланец приварной')

    , ('00000000-0000-0000-0000-directory005', 'A', 'наличие механического ограничителя хода поршня')
    , ('00000000-0000-0000-0000-directory005', 'K', 'возможность регулировки межцентрового расстояния')
    , ('00000000-0000-0000-0000-directory005', 'C', 'с замедлительным клапаном')
    , ('00000000-0000-0000-0000-directory005', 'F', 'фланцевое крепление крышки передней')
    , ('00000000-0000-0000-0000-directory005', 'PT', 'гидроцилиндр плуга оборотного')
    , ('00000000-0000-0000-0000-directory005', 'D', 'наличие демпферного устройства')

    , ('00000000-0000-0000-0000-directory006', 'T', 'тропический климат')
    , ('00000000-0000-0000-0000-directory006', 'YXL', 'умеренно-холодный климат')
    , ('00000000-0000-0000-0000-directory006', 'XL', 'холодный климат')
    , ('00000000-0000-0000-0000-directory006', 'Y', 'умеренный климат')
;

INSERT INTO template_keys (template_id, name, description, pattern, default_value, directory_id)
VALUES
    ('00000000-0000-0000-0000-template0001', 'series', 'Серия', 'Серия поршневых одноступенчатых гидроцилиндров на шпильках (болтах)', '', NULL)
    , ('00000000-0000-0000-0000-template0001', 'D', 'Диаметр цилиндра', 'Диаметр цилиндра {value} мм', '', NULL)
    , ('00000000-0000-0000-0000-template0001', 'd', 'Диаметр штока', 'Диаметр штока {value} мм', '', NULL)
    , ('00000000-0000-0000-0000-template0001', 'S', 'Ход поршня', 'Ход поршня {value} мм', '', NULL)
    , ('00000000-0000-0000-0000-template0001', 'pressure', 'Исполнение по номинальному давлению', '', '', '00000000-0000-0000-0000-directory002')
    , ('00000000-0000-0000-0000-template0001', 'attachment', 'Исполнение по способу крепления гидроцилиндров', '', '', '00000000-0000-0000-0000-directory003')
    , ('00000000-0000-0000-0000-template0001', 'working_fluid', 'Исполнение по подводу рабочей жидкости', '', 'Бонка с внутренней резьбой', '00000000-0000-0000-0000-directory004')
    , ('00000000-0000-0000-0000-template0001', 'hydraulic_cylinder', 'Конструктивное исполнение гидроцилиндра', '', '', '00000000-0000-0000-0000-directory005')
    , ('00000000-0000-0000-0000-template0001', 'climatic', 'Климатическое исполнение', '', 'Тропический климат', '00000000-0000-0000-0000-directory006')
    , ('00000000-0000-0000-0000-template0001', 'L', 'Межцентровое расстояние', 'Межцентровое расстояние {value} мм', '', NULL)
    , ('00000000-0000-0000-0000-template0001', 'supply_hydraulic_cylinders', 'Вариант поставки гидроцилиндра', '{value}', '', NULL)

    , ('00000000-0000-0000-0000-template0002', 'series', 'Серия', 'Серия поршневых одноступенчатых гидроцилиндров', '', NULL)
    , ('00000000-0000-0000-0000-template0002', 'D', 'Диаметр цилиндра', 'Диаметр цилиндра {value} мм', '', NULL)
    , ('00000000-0000-0000-0000-template0002', 'd', 'Диаметр штока', 'Диаметр штока {value} мм', '', NULL)
    , ('00000000-0000-0000-0000-template0002', 'S', 'Ход поршня', 'Ход поршня {value} мм', '', NULL)
    , ('00000000-0000-0000-0000-template0002', 'pressure', 'Исполнение по номинальному давлению', '', '', '00000000-0000-0000-0000-directory002')
    , ('00000000-0000-0000-0000-template0002', 'attachment', 'Исполнение по способу крепления гидроцилиндров', '', '', '00000000-0000-0000-0000-directory003')
    , ('00000000-0000-0000-0000-template0002', 'working_fluid', 'Исполнение по подводу рабочей жидкости', '', 'Бонка с внутренней резьбой', '00000000-0000-0000-0000-directory004')
    , ('00000000-0000-0000-0000-template0002', 'hydraulic_cylinder', 'Конструктивное исполнение гидроцилиндра', '', 'Отсутствие данных конструктивных исполнений', '00000000-0000-0000-0000-directory005')
    , ('00000000-0000-0000-0000-template0002', 'climatic', 'Климатическое исполнение', '', 'Тропический климат', '00000000-0000-0000-0000-directory006')
    , ('00000000-0000-0000-0000-template0002', 'L', 'Межцентровое расстояние', 'Межцентровое расстояние {value} мм', '', NULL)
    , ('00000000-0000-0000-0000-template0002', 'supply_hydraulic_cylinders', 'Вариант поставки гидроцилиндра', '{value}', '', NULL)

    , ('00000000-0000-0000-0000-template0003', 'series', 'Серия', 'Серия плунжерных одноступенчатых гидроцилиндров', '', NULL)
    , ('00000000-0000-0000-0000-template0003', 'd', 'Диаметр плунжера', 'Диаметр плунжера {value} мм', '', NULL)
    , ('00000000-0000-0000-0000-template0003', 'S', 'Ход плунжера', 'Ход плунжера {value} мм', '', NULL)
    , ('00000000-0000-0000-0000-template0003', 'pressure', 'Исполнение по номинальному давлению', '', '', '00000000-0000-0000-0000-directory002')
    , ('00000000-0000-0000-0000-template0003', 'attachment', 'Исполнение по способу крепления гидроцилиндров', '', '', '00000000-0000-0000-0000-directory003')
    , ('00000000-0000-0000-0000-template0003', 'working_fluid', 'Исполнение по подводу рабочей жидкости', '', 'Бонка с внутренней резьбой', '00000000-0000-0000-0000-directory004')
    , ('00000000-0000-0000-0000-template0003', 'hydraulic_cylinder', 'Конструктивное исполнение гидроцилиндра', '', 'Отсутствие данных конструктивных исполнений', '00000000-0000-0000-0000-directory005')
    , ('00000000-0000-0000-0000-template0003', 'climatic', 'Климатическое исполнение', '', 'Тропический климат', '00000000-0000-0000-0000-directory006')
    , ('00000000-0000-0000-0000-template0003', 'L', 'Межцентровое расстояние', 'Межцентровое расстояние {value} мм', '', NULL)
    , ('00000000-0000-0000-0000-template0003', 'supply_hydraulic_cylinders', 'Вариант поставки гидроцилиндра', '{value}', '', NULL)
;
