from utils.db_operations import save_in_db, get_in_db
from utils.paginatsiya import pagination
from models.transfers import Transfers


def all_transfers(search, page, limit, db):
    transfers = db.query(Transfers)
    if search:
        search_formatted = "%{}%".format(search)
        transfers = transfers.filter(Transfers.name.like(search_formatted))
    # else:
    #     transfers = transfers.id > 0
    transfers = transfers.order_by(Transfers.name.asc())
    return pagination(transfers, page, limit)


def create_transfers_y(form, db,this_user):
    new_transfers_db = Transfers(
        name=form.name,
        product_id=form.product_id,
        quantity=form.quantity,
        date=form.date,
        warehoueser_id=form.warehoueser_id,
        driver_id=form.driver_id,
        status=form.status

    )
    save_in_db(db, new_transfers_db)


def update_transfers_y(form,db,this_user):
    if get_in_db(db, Transfers, form.id):
        db.query(Transfers).filter(Transfers.id == form.id).update({
            Transfers.id: form.id,
            Transfers.name: form.name,
            Transfers.product_id: form.product_id,
            Transfers.quantity: form.quantity,
            Transfers.date: form.date,
            Transfers.warehoueser_id: form.warehoueser_id,
            Transfers.driver_id: form.driver_id,
            Transfers.status: form.status
        })
        db.commit()

def delete_transfers_r(id, db):
    get_in_db(db, Transfers, id)
    db.query(Transfers).filter(Transfers.id == id).delete()
    db.commit()