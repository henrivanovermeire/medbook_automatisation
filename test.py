from medbook_processor import MedbookProcessor


medbook = MedbookProcessor()

medbook.upload_case(date_of_birth="01-01-2000", procedure="Testprocedure", specialty="10")
medbook.driver.close()
